from configs.names_config import LOWER_CASE_LIST, UPPER_CASE_LIST, AUX_CHARS_DICT
from utils.preprocessing import read_unique_names
import numpy as np


characters_list = LOWER_CASE_LIST + UPPER_CASE_LIST + list(AUX_CHARS_DICT.values())
surnames_list = read_unique_names('surnames').tolist()


def select_character(probs_array):  # Given probability array, randomly select character accordingly.
    return np.random.choice(characters_list, size=1, p=probs_array)[0]  # [0] gets item from returned list.


def select_surnames(size):  # Randomly select surname(s) with uniform probability.
    return np.random.choice(surnames_list, size=size)  # Return entire list for remix preference.


def adjust_creation(created_name):  # Replace start_char with empty space. Ensure creation is capitalized.
    created_name = created_name.replace(AUX_CHARS_DICT['start'], '').capitalize()
    if created_name[:2] == 'Mc':  # If created name starts with Mc, capitalize 3rd letter.
        created_name = created_name[:2] + created_name[2:].capitalize()
    return created_name
