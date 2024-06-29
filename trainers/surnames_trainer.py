from configs.paths_config import DATA_FOLDER_PATH, MODELS_FOLDER_PATH
from configs.models_config import EPOCHS, DENOMINATOR
from configs.names_config import AUX_CHARS_DICT, MAX_SURNAME_LEN
from neural_nets.stacked_lstm import make_stacked_lstm
from utils.files_helper import read_unique_names
from utils.embeddings import concat_arrays, encode_seqs, encode_name
from utils.candidates import select_character, adjust_creation
import os
import json
from keras import metrics, models, backend
from keras.callbacks import EarlyStopping


class SurnamesTrainer:
    """
    Train and evaluate Keras model on surnames.

    Attributes:
        names_series (pd.Series): series of unique surnames.
        encoding_info_path (str): path to encoding information file.
        model_path (str): path to surname's model file.
        metrics_list (list): list of metrics used during training epoch.

    Methods:
        train(): train model on surnames.
        evaluate(num_names: int, top_k_elements: int = None): generate a number of new names.
    """

    def __init__(self):
        """
        Initialize with series of unique surnames, paths to encoding information and model files,
        and a list of metrics used during training.
        """
        self.names_series = read_unique_names("surnames")
        self.encoding_info_path = os.path.join(
            DATA_FOLDER_PATH, "encoding_info.json"
        )
        self.model_path = os.path.join(
            MODELS_FOLDER_PATH, "surnames.h5"
        )
        self.metrics_list = [metrics.CategoricalAccuracy(name="categorical_accuracy")]

    def train(self):
        """
        Train model on surnames.
        """
        # Timesteps (encoding length) = max name length + 1 (start_char).
        timesteps = max(self.names_series.apply(lambda x: len(x))) + 1

        # Make list of encoded matrices/vectors list to a concatenated matrix/vector.
        seqs_matrix = sum(
            self.names_series.apply(lambda x: encode_name(x, timesteps)).tolist(), []
        )
        seqs_matrix = concat_arrays(
            seqs_matrix
        )  # Seqs shape: (samples, timesteps, features).

        chars_matrix = sum(
            self.names_series.apply(lambda x: encode_name(x, timesteps, False)).tolist(), []
        )
        chars_matrix = concat_arrays(chars_matrix)  # Chars shape: (samples, features).

        file = open(self.encoding_info_path, "r")
        encoding_info_dict = json.load(file)  # Read encoding info to make updates.
        file.close()

        encoding_info_dict.update(
            {
                "surnames": {
                    "timesteps": seqs_matrix.shape[1],
                    "features": seqs_matrix.shape[-1],
                }
            }
        )

        file = open(self.encoding_info_path, "w")
        json.dump(encoding_info_dict, file)  # Save updated encoding info.
        file.close()

        try:  # If pre-trained model is found.
            model = models.load_model(self.model_path)
            backend.clear_session()

        except OSError:  # Input shape is 2nd and 3rd elements of seqs shape.
            model = make_stacked_lstm(seqs_matrix.shape[1:], self.metrics_list)

        # Call back patience = epochs // denominator.
        early_stopping = EarlyStopping(
            monitor=self.metrics_list[0].name, patience=EPOCHS // DENOMINATOR, verbose=0
        )
        model.fit(
            x=seqs_matrix, y=chars_matrix, epochs=EPOCHS, callbacks=[early_stopping]
        )
        model.save(self.model_path)
        backend.clear_session()

    def evaluate(self, num_names: int, top_k_elements: int = None):
        """
        Create a number of new surnames for evaluation.

        Args:
            num_names (int): number of new names to create.
            top_k_elements (int, optional): number of top characters for selection during creation.

        Returns:
            str: string of all created names, separated by commas.
        """
        # Chars to be added at start and end.
        start_char, end_char = AUX_CHARS_DICT["start"], AUX_CHARS_DICT["end"]

        model = models.load_model(self.model_path)  # Load pre-trained model.
        backend.clear_session()

        file = open(self.encoding_info_path, "r")
        timesteps = json.load(file)["surnames"]["timesteps"]
        file.close()

        creations, existing_names = [], self.names_series.tolist()

        while len(creations) < num_names:
            creation_iter = start_char  # Each creation starts from start_char.
            while True:
                seqs_matrix = encode_seqs(
                    creation_iter, timesteps
                )  # Encode creation into 3-D sequences matrix.

                pred_vector = model.predict(
                    seqs_matrix, verbose=0
                )  # Prediction is 2-D vector.

                char_iter = select_character(
                    pred_vector[0], top_k_elements
                )  # [0] gets 1-D probability array.

                if char_iter == end_char:  # Iterated creation stops at end_char.
                    break

                if {char_iter} == set(creation_iter[-2:]):  # Prevent 3 straight identical letters.
                    continue

                creation_iter += char_iter  # Append selection to creation.
                if len(creation_iter) == MAX_SURNAME_LEN:  # Control length.
                    break

            creation_iter = adjust_creation(creation_iter)
            if len(creation_iter.strip()) > 0:  # Ensure creation isn't empty.
                # Ensure creation isn't already existing.
                if creation_iter not in existing_names + creations:
                    creations.append(creation_iter)

        return ", ".join(creations)


if __name__ == "__main__":
    trainer = SurnamesTrainer()
    # trainer.train()
    print(f"Evaluations:\n{trainer.evaluate(5, 15)}")
