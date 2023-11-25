from configs.app_config import APP_BASE_PATH
from configs.names_config import AUX_CHARS_DICT, MAX_FORENAME_LEN
from utils.preprocessing import read_unique_names
from utils.embeddings import encode_seqs
from utils.candidates import select_character, adjust_creation
import os
import json
from keras import models, backend


class ForenameCreator:
    """You never know what your parents are gonna "give" you."""

    def __init__(self, gender):  # Gender options: male, female.
        self.gender = gender
        self.names_series = read_unique_names(f'{self.gender}_forenames')
        self.encoding_info_path = os.path.join(APP_BASE_PATH, 'data', 'encoding_info.json')

        model_path = os.path.join(APP_BASE_PATH, 'models', f'{self.gender}_forenames.h5')
        self.model = models.load_model(model_path)
        backend.clear_session()

    def create(self, number, lock):  # Number of names to be created.
        start_char, end_char = AUX_CHARS_DICT['start'], AUX_CHARS_DICT['end']  # Chars to be added at start and end.

        lock.acquire()
        try:
            file = open(self.encoding_info_path, 'r')
            timesteps = json.load(file)[f'{self.gender}_forenames']['timesteps']  # Read forenames' encoding info.
            file.close()

        finally:
            lock.release()

        creations_list, existing_list = [], self.names_series.tolist()  # List of new creations and existing names.

        while len(creations_list) < number:  # Make creations according to number argument.
            creation_iter = start_char  # Each creation starts from start_char.
            while True:
                seqs_matrix = encode_seqs(creation_iter, timesteps)  # Encode creation into 3-D sequences matrix.
                pred_vector = self.model.predict(seqs_matrix, verbose=0)  # Prediction is 2-D vector.
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

        return creations_list


if __name__ == '__main__':
    import threading

    lock_main = threading.Lock()

    creator = ForenameCreator('female')
    print(f'Creations:\n{creator.create(5, lock_main)}')
