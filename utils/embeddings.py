from configs.names_config import LOWER_CASE_LIST, UPPER_CASE_LIST, AUX_CHARS_DICT, SEQUENCE_WINDOW
from configs.models_config import PAD_VALUE
import numpy as np


characters_list = LOWER_CASE_LIST + UPPER_CASE_LIST + list(AUX_CHARS_DICT.values())  # List of all chars.
chars2int_dict = dict(zip(characters_list, set(range(len(characters_list)))))  # Dictionary to map chars to int.
int2chars_dict = {v: k for k, v in chars2int_dict.items()}  # Dictionary to map int to chars.

start_char = AUX_CHARS_DICT['start']  # Char to be added at leftmost edge to represent name's start.
end_char = AUX_CHARS_DICT['end']  # Char to be added at rightmost edge to represent name's end.


def concat_arrays(arrays_list):  # Concatenate list of arrays with respect to axis 0.
    return np.concatenate(arrays_list, axis=0)


def encode_seqs(string, timesteps):  # Encode string to 3-D sequences of shape (1, timesteps, len(characters_list)).
    seqs_matrix = np.zeros((1, timesteps, len(characters_list)))  # Matrix starts from zeros.

    pre_padding_len = timesteps - len(string)  # Number of pre-padding chars at left side.
    seqs_matrix[0, :pre_padding_len, :] = PAD_VALUE  # Do pre-padding on 2nd and 3rd dimensions.

    items_list = list(string)  # List of all items from string.
    for index, item in enumerate(items_list):  # Encode through items list and its index.
        # 2nd dimension's iterated index: pre_padding_len + iterated index.
        # 3rd dimension's iterated index: iterated item's pairing int.
        seqs_matrix[0, pre_padding_len + index, chars2int_dict[item]] = 1
    return seqs_matrix


def encode_chars(string):  # Encode string to 2-D chars of shape (1, len(characters_list)).
    chars_vector = np.zeros((1, len(characters_list)))  # Vector starts from zeros.

    items_list = list(string)  # List of all items from string.
    for item in items_list:  # Encode through items list.
        chars_vector[0, chars2int_dict[item]] = 1  # 2nd dimension's iterated index: iterated item's pairing int.
    return chars_vector


def decode_matrix(matrix):  # Decode 3-D matrix of shape (1, timesteps, len(chars_list)) to string.
    items_list = []  # List of decoded items.

    matrix = matrix[0]  # [0] gets the matrix formed by 2nd and 3rd dimensions.
    for row in matrix:
        if 1 in row:  # If 1 is in iterated row vector.
            index = np.where(row == 1)[0][0]  # [0][0] gets index of the column which has 1 in iterated row.
            items_list.append(int2chars_dict[index])  # Map index to char and append to list.

    string = ''.join(items_list)  # Join items list to string. Replace start_char and end_char with empty space.
    return string.replace(start_char, '').replace(end_char, '')


def encode_name(name, timesteps, to_seqs=True):  # Encode input name to sequences or chars.
    # For example: encoded sequences of 'Hi' are: ~, ~H, ~Hi; encoded chars are: H, i, #.
    name = start_char + name + end_char  # Add start_char at front and end_char at back.

    output_list = []  # List of encoded matrices/vectors.
    for i in range(1, len(name)):  # Iterate through sliced substring of name.
        if to_seqs:  # If the wanted output is encoded sequences, apply max function to adjust for window.
            output_list.append(encode_seqs(name[max(i - SEQUENCE_WINDOW, 0):i], timesteps))

        else:  # If the wanted output is encoded chars.
            output_list.append(encode_chars(name[i]))

    return output_list


if __name__ == '__main__':
    from utils.decomposition import decompose_names
    import time

    names_series = decompose_names('forename')

    start = time.time()

    steps = max(names_series.apply(lambda x: len(x))) + 1  # Timesteps is max name length plus 1, indicating start_char.
    matrices = names_series.apply(lambda x: encode_seqs(x, steps))

    for original_name, encoded_matrix in zip(names_series, matrices):  # Check each encoding validity.
        if original_name != decode_matrix(encoded_matrix):  # Print wrong encoding if found.
            print('Incorrect encoding for name ' + original_name + '!')

    # Make list of encoded matrices/vectors list to a matrices/vectors list.
    seqs_list = sum(names_series.apply(lambda x: encode_name(x, steps)).tolist(), [])
    chars_list = sum(names_series.apply(lambda x: encode_name(x, steps, False)).tolist(), [])

    for seqs, chars in zip(seqs_list, chars_list):  # 1st assertion: shape of each encoded seqs and chars.
        assert seqs.shape == (1, steps, len(characters_list)), chars.shape == (1, len(characters_list))

    # 2nd assertion: len(seqs_list) = length of all names + total names count; an n-length name gets n + 1 sequences.
    assert len(seqs_list) == len(''.join(names_series.tolist())) + len(names_series)

    end = time.time()
    print('\nTotal running time: ' + str(round(end - start, 2)) + ' seconds.')
