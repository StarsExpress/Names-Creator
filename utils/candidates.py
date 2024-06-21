from configs.names_config import LOWER_CASE_LIST, UPPER_CASE_LIST, AUX_CHARS_DICT
from utils.files_helper import read_unique_names
import numpy as np


characters_list = LOWER_CASE_LIST + UPPER_CASE_LIST + list(AUX_CHARS_DICT.values())
surnames_list = read_unique_names('surnames').tolist()


def select_character(probs_array: np.ndarray, top_k_elements: int = None):
    """
    Select a character based on provided probabilities.
    If top_k_elements is provided, only top k chars of highest probs are considered.

    Args:
        probs_array (np.ndarray): array of probs for each character.
        top_k_elements (int, optional): top k chars to be considered. Defaults to None.

    Returns:
        str: selected char.
    """
    if top_k_elements is None:  # None means no top-k method.
        return np.random.choice(characters_list, size=1, p=probs_array)[0]  # [0] gets item from returned list.

    top_k_indices = probs_array.argsort()[-top_k_elements:]
    top_k_probs = probs_array[top_k_indices]
    top_k_probs *= 1 / top_k_probs.sum()  # Normalize sum of selected probabilities to 1.
    top_k_characters = np.array(characters_list)[top_k_indices]
    return np.random.choice(top_k_characters, size=1, p=top_k_probs)[0]


def select_surnames(size: int):
    """
    Select a number of surnames with uniform probability.

    Args:
        size (int): number of surnames to select.

    Returns:
        np.ndarray: array of selected surnames.
    """
    return np.random.choice(surnames_list, size=size)  # Return entire list for remix preference.


def adjust_creation(creation: str):
    """
    Adjust the created name by replacing start_char with an empty space and capitalizing name.
    If created name starts with 'Mc', 3rd letter is also capitalized.

    Args:
        creation (str): the created name to adjust.

    Returns:
        str: adjusted name.
    """
    creation = creation.replace(AUX_CHARS_DICT['start'], '').capitalize()
    if creation[:2] == 'Mc':
        creation = creation[:2] + creation[2:].capitalize()
    return creation
