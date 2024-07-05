import os
import pandas as pd
from configs.paths_config import DATA_FOLDER_PATH


def read_unique_names(name_type: str):
    """
    Read unique names from a specified file.

    If names aren't unique, it removes duplicates and saves unique names back to the read file.

    Args:
        name_type (str): type of names to read. Can be: 'male_forenames', 'female_forenames', 'surnames'.

    Returns:
        pd.Series: series of unique names.
    """
    names_file_path = os.path.join(DATA_FOLDER_PATH, name_type)
    names_df = pd.read_csv(names_file_path, sep='\t', header=None, names=['names'])

    if names_df['names'].is_unique is False:
        names_df.drop_duplicates(inplace=True)
        names_df.reset_index(drop=True, inplace=True)
        names_df.to_csv(names_file_path, header=False, index=False)

    return names_df['names']  # Return series.


def encode_names_list_to_csv(gender: str, names: list[str]):
    """
    Take a list of names and a gender, and return CSV of names.

    Args:
        gender (str): gender of names. Used as header in the text string.
        names (list[str]): list of names to turn into text.

    Returns:
        bytes: encoded CSV.
    """
    names_df = pd.DataFrame(names, columns=[f'{gender.capitalize()} Names'])
    return names_df.to_csv(index=False).encode('utf-8')


def turn_names_list_to_txt(gender: str, names: list[str]):
    """
    Take a list of names and a gender, and return a text string with each name on a new line.

    Args:
        gender (str): gender of names. Used as header in the text string.
        names (list[str]): list of names to turn into text.

    Returns:
        str: text string of names.
    """
    return '\n'.join([f'{gender.capitalize()} Names'] + names)
