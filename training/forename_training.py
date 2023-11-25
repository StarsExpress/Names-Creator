from configs.app_config import APP_BASE_PATH
from configs.models_config import EPOCHS, DENOMINATOR
from configs.names_config import AUX_CHARS_DICT, MAX_FORENAME_LEN
from neural_nets.stacked_lstm import make_stacked_lstm
from utils.preprocessing import read_unique_names
from utils.embeddings import concat_arrays, encode_seqs, encode_name
from utils.candidates import select_character, adjust_creation
import os
import json
from keras import metrics, models, backend
from keras.callbacks import EarlyStopping


class ForenameTrainer:
    """Train and evaluate Keras model on forenames."""

    def __init__(self, gender):  # Gender options: male, female.
        self.gender = gender
        self.names_series = read_unique_names(f'{self.gender}_forenames')
        self.encoding_info_path = os.path.join(APP_BASE_PATH, 'data', 'encoding_info.json')
        self.model_path = os.path.join(APP_BASE_PATH, 'models', f'{self.gender}_forenames.h5')
        self.metrics_list = [metrics.CategoricalAccuracy(name='categorical_accuracy')]

    def train(self):
        # Timesteps, the encoding length, is the max name length plus 1, indicating start_char.
        timesteps = max(self.names_series.apply(lambda x: len(x))) + 1

        # Make list of encoded matrices/vectors list to a concatenated matrix/vector.
        seqs_matrix = sum(self.names_series.apply(lambda x: encode_name(x, timesteps)).tolist(), [])
        seqs_matrix = concat_arrays(seqs_matrix)  # Seqs shape: (samples, timesteps, features).
        chars_matrix = sum(self.names_series.apply(lambda x: encode_name(x, timesteps, False)).tolist(), [])
        chars_matrix = concat_arrays(chars_matrix)  # Chars shape: (samples, features).

        file = open(self.encoding_info_path, 'r')
        encoding_info_dict = json.load(file)  # Read encoding info to make updates.
        file.close()

        encoding_info_dict.update({f'{self.gender}_forenames': {'timesteps': seqs_matrix.shape[1],
                                                                'features': seqs_matrix.shape[-1]}})

        file = open(self.encoding_info_path, 'w')
        json.dump(encoding_info_dict, file)  # Save updated encoding info.
        file.close()

        try:  # If pre-trained model is found, directly load it.
            model = models.load_model(self.model_path)
            backend.clear_session()

        except OSError:  # If not found, rebuild model. Input shape is 2nd and 3rd elements of seqs shape.
            model = make_stacked_lstm(seqs_matrix.shape[1:], self.metrics_list)

        # Call back patience = epochs // denominator.
        early_stopping = EarlyStopping(monitor=self.metrics_list[0].name, patience=EPOCHS // DENOMINATOR, verbose=0)
        model.fit(x=seqs_matrix, y=chars_matrix, epochs=EPOCHS, callbacks=[early_stopping])
        model.save(self.model_path)
        backend.clear_session()

    def evaluate(self, number):  # Number of created names to be evaluated.
        start_char, end_char = AUX_CHARS_DICT['start'], AUX_CHARS_DICT['end']  # Chars to be added at start and end.

        model = models.load_model(self.model_path)  # Load pre-trained model.
        backend.clear_session()

        file = open(self.encoding_info_path, 'r')
        timesteps = json.load(file)[f'{self.gender}_forenames']['timesteps']  # Read forenames' encoding info.
        file.close()

        creations_list, existing_list = [], self.names_series.tolist()  # List of new creations and existing names.

        while len(creations_list) < number:  # Make creations according to number argument.
            creation_iter = start_char  # Each creation starts from start_char.
            while True:
                seqs_matrix = encode_seqs(creation_iter, timesteps)  # Encode creation into 3-D sequences matrix.
                pred_vector = model.predict(seqs_matrix, verbose=0)  # Prediction is 2-D vector.
                char_iter = select_character(pred_vector[0])  # [0] gets 1-D probability array.
                if char_iter == end_char:  # Iterated creation stops at end_char.
                    break

                if {char_iter} == set(creation_iter[-2:]):  # Prevent 3 straight identical letters.
                    continue

                creation_iter += char_iter  # Append selection to creation.
                if len(creation_iter) == MAX_FORENAME_LEN:  # Control iterated creation length.
                    break

            creation_iter = adjust_creation(creation_iter)
            if len(creation_iter.strip()) > 0:  # Ensure creation isn't empty.
                if creation_iter not in existing_list + creations_list:  # Ensure creation isn't already existing.
                    creations_list.append(creation_iter)

        return ', '.join(creations_list)  # Return all creations joined string.


if __name__ == '__main__':
    import time

    start = time.time()
    trainer = ForenameTrainer('male')
    trainer.train()
    print(f'Evaluations:\n{trainer.evaluate(5)}')

    end = time.time()
    print(f'\nTotal running time: {str(round(end - start, 2))} seconds.')
