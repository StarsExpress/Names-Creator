from utils.embeddings import encode_seqs, decode_matrix, encode_name, characters_list
from utils.files_helper import read_unique_names


def test_embeddings(names_type: str):
    """
    Test functionality of embeddings.py in these steps:
    1. Read unique names of a specified type and encode them into sequences.
    2. Decode encoded sequences and check if decoded names match original names.
    3. Also check shapes of encoded sequences and characters.

    Args:
        names_type (str): type of names to test. Can be 'surnames', 'male_forenames', or 'female_forenames'.
    """
    names_series = read_unique_names(names_type)

    # Plus 1 indicates start_char.
    steps = max(names_series.apply(lambda x: len(x))) + 1
    matrices = names_series.apply(lambda x: encode_seqs(x, steps))

    for original_name, encoded_matrix in zip(names_series, matrices):  # Check each encoding validity.
        if original_name != decode_matrix(encoded_matrix):  # If wrong encoding is found.
            print(f'Incorrect encoding for name {original_name}!')

    # Make list of encoded matrices/vectors list to a matrices/vectors list.
    seqs_list = sum(names_series.apply(lambda x: encode_name(x, steps)).tolist(), [])
    chars_list = sum(names_series.apply(lambda x: encode_name(x, steps, False)).tolist(), [])

    for seqs, chars in zip(seqs_list, chars_list):  # Check shapes of encoded seqs and chars.
        assert seqs.shape == (1, steps, len(characters_list)), chars.shape == (1, len(characters_list))

    # len(seqs_list) = length of all names + total names count; n-length name gets n + 1 seqs.
    assert len(seqs_list) == len(''.join(names_series.tolist())) + len(names_series)


if __name__ == '__main__':
    import time

    start = time.time()
    test_embeddings('surnames')
    test_embeddings('male_forenames')
    test_embeddings('female_forenames')
    end = time.time()
    print(f'\nTotal runtime: {str(round(end - start, 2))} seconds.')
