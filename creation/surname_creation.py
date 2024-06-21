from configs.app_config import APP_BASE_PATH
from configs.names_config import AUX_CHARS_DICT, MAX_SURNAME_LEN
from utils.files_helper import read_unique_names
from utils.embeddings import encode_seqs
from utils.candidates import select_character, adjust_creation
import os
import json
from keras import models, backend


class SurnameCreator:
    """
    Create new surnames via pre-trained Keras model.

    Attributes:
    encoding_info_path (str): path to encoding information file.
    model_path (str): path to surname's model file of.

    Methods:
    create(names_num: int, top_k_elements: int = None): create a number of new surnames.
    """

    def __init__(self):
        """
        Initialize with series of unique surnames, paths to encoding information and model files.
        """
        self.names_series = read_unique_names('surnames')
        self.encoding_info_path = os.path.join(APP_BASE_PATH, 'data', 'encoding_info.json')

        model_path = os.path.join(APP_BASE_PATH, 'models', 'surnames.h5')
        self.model = models.load_model(model_path)
        backend.clear_session()

    def create(self, names_num: int, top_k_elements: int = None):
        """
        Create a number of new surnames for production.

        Args:
            names_num (int): number of new names to create.
            top_k_elements (int, optional): number of top characters for selection during creation.

        Returns:
            str: string of all created names, separated by commas.
        """
        # Chars to be added at start and end.
        start_char, end_char = AUX_CHARS_DICT['start'], AUX_CHARS_DICT['end']

        file = open(self.encoding_info_path, 'r')
        timesteps = json.load(file)['surnames']['timesteps']
        file.close()

        creations, existing_names = [], self.names_series.tolist()

        while len(creations) < names_num:
            creation_iter = start_char  # Each creation starts from start_char.
            while True:
                seqs_matrix = encode_seqs(creation_iter, timesteps)  # Encode creation into 3-D sequences matrix.
                pred_vector = self.model.predict(seqs_matrix, verbose=0)  # Prediction is 2-D vector.
                char_iter = select_character(pred_vector[0], top_k_elements)  # [0] gets 1-D probability array.
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

        return creations


if __name__ == '__main__':
    creator = SurnameCreator()
    print(f'Creations:\n{creator.create(5, 10)}')
