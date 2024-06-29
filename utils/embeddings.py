from configs.names_config import LOWER_CASE_LIST, UPPER_CASE_LIST, AUX_CHARS_DICT, SEQUENCE_WINDOW
from configs.models_config import PAD_VALUE
import numpy as np


characters_list = LOWER_CASE_LIST + UPPER_CASE_LIST + list(AUX_CHARS_DICT.values())
chars2int_dict = dict(zip(characters_list, set(range(len(characters_list)))))
int2chars_dict = {v: k for k, v in chars2int_dict.items()}

start_char = AUX_CHARS_DICT['start']  # Added at leftmost edge to represent name's start.
end_char = AUX_CHARS_DICT['end']  # Added at rightmost edge to represent name's end.


def concat_arrays(arrays_list: list[np.ndarray]):
    """
    Concatenate list of arrays vertically.

    Args:
        arrays_list (list[np.ndarray]): list of arrays to concatenate.

    Returns:
        np.ndarray: concatenated array.
    """
    return np.concatenate(arrays_list, axis=0)


def encode_seqs(string: str, timesteps: int):
    """
    Encode a string into a 3-D sequence of shape (1, timesteps, len(characters_list)).

    Args:
        string (str): string to encode.
        timesteps (int): number of timesteps for sequence.

    Returns:
        np.ndarray: encoded 3-D sequence.
    """
    seqs_matrix = np.zeros((1, timesteps, len(characters_list)))  # Matrix starts from zeros.

    pre_padding_len = timesteps - len(string)  # Number of pre-padding chars at left side.
    seqs_matrix[0, :pre_padding_len, :] = PAD_VALUE  # Do pre-padding on 2nd and 3rd dimensions.

    items_list = list(string)  # List of all items from string.
    for idx, item in enumerate(items_list):  # Encode through items list and its idx.
        # 2nd dimension's iterated idx: pre_padding_len + iterated idx.
        # 3rd dimension's iterated idx: iterated item's pairing int.
        seqs_matrix[0, pre_padding_len + idx, chars2int_dict[item]] = 1
    return seqs_matrix


def encode_chars(string: str):
    """
    Encode a string into a 2-D array of shape (1, len(characters_list)).

    Args:
        string (str): string to encode.

    Returns:
        np.ndarray: encoded 2-D array.
    """
    chars_vector = np.zeros((1, len(characters_list)))  # Vector starts from zeros.

    items_list = list(string)  # List of all items from string.
    for item in items_list:  # Encode through items list.
        chars_vector[0, chars2int_dict[item]] = 1  # 2nd dimension's iterated idx: iterated item's pairing int.
    return chars_vector


def decode_matrix(matrix: np.ndarray):
    """
    Decode a 3-D matrix of shape (1, timesteps, len(chars_list)) into a string.

    Args:
        matrix (np.ndarray): matrix to decode.

    Returns:
        str: decoded string.
    """
    items_list = []  # List of decoded items.

    matrix = matrix[0]  # [0] gets the matrix formed by 2nd and 3rd dimensions.
    for row in matrix:
        if 1 in row:  # If 1 is in iterated row vector.
            idx = np.where(row == 1)[0][0]  # [0][0] gets idx of the column having 1 in iterated row.
            items_list.append(int2chars_dict[idx])  # Map idx to char and append to list.

    string = ''.join(items_list)  # Replace start_char and end_char with empty space.
    return string.replace(start_char, '').replace(end_char, '')


def encode_name(name: str, timesteps: int, to_seqs: bool = True):
    """
    Encode a name into sequences or characters.
    For example: encoded sequences of 'Hi' are: ~, ~H, ~Hi; encoded chars are: H, i, #.

    Args:
        name (str): name to encode.
        timesteps (int): number of timesteps for sequence.
        to_seqs (bool, optional): if True, encode to sequences. Otherwise, encode to chars. Defaults to True.

    Returns:
        list: list of encoded matrices/vectors.
    """
    name = start_char + name + end_char  # Add start_char at front and end_char at back.

    encoded_output = []
    for i in range(1, len(name)):  # Iterate through sliced substring of name.
        if to_seqs:  # If the wanted output is encoded sequences, apply max function to adjust for window.
            encoded_output.append(encode_seqs(name[max(i - SEQUENCE_WINDOW, 0):i], timesteps))

        else:
            encoded_output.append(encode_chars(name[i]))

    return encoded_output
