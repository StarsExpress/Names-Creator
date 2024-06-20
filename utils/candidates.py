from configs.names_config import LOWER_CASE_LIST, UPPER_CASE_LIST, AUX_CHARS_DICT
from utils.preprocessing import read_unique_names
import numpy as np


characters_list = LOWER_CASE_LIST + UPPER_CASE_LIST + list(AUX_CHARS_DICT.values())
surnames_list = read_unique_names('surnames').tolist()


def select_character(
        probs_array: np.ndarray,
        top_k_elements: int = None
):
    if top_k_elements is None:  # None means no top-k method.
        return np.random.choice(characters_list, size=1, p=probs_array)[0]  # [0] gets item from returned list.

    top_k_indices = probs_array.argsort()[-top_k_elements:]
    top_k_probs = probs_array[top_k_indices]
    top_k_probs *= 1 / top_k_probs.sum()  # Normalize sum of selected probabilities to 1.
    top_k_characters = np.array(characters_list)[top_k_indices]
    return np.random.choice(top_k_characters, size=1, p=top_k_probs)[0]


def select_surnames(size: int):  # With uniform probability.
    return np.random.choice(surnames_list, size=size)  # Return entire list for remix preference.


def adjust_creation(created_name: str):
    # Replace start_char with empty space. Ensure creation is capitalized.
    created_name = created_name.replace(AUX_CHARS_DICT['start'], '').capitalize()
    if created_name[:2] == 'Mc':  # If created name starts with Mc, capitalize 3rd letter.
        created_name = created_name[:2] + created_name[2:].capitalize()
    return created_name
