from configs.app_config import APP_BASE_PATH
from configs.names_config import ROMAN_SUFFIX_SET, ENGLISH_SUFFIX_SET, DF_COLS_LIST
import os
import pandas as pd


names_file_path = os.path.join(APP_BASE_PATH, 'data', 'names')
names_df = pd.read_csv(names_file_path, sep='\t', header=None, names=['names'])


def split_name(name):  # Split input name to find given & family name plus suffix.
    split_list = name.split()

    # If the last item is suffix.
    if (set(split_list[-1]) - ROMAN_SUFFIX_SET == set()) | (split_list[-1] in ENGLISH_SUFFIX_SET):
        # String 1st to (n - 2)th item as entire given name. Return family name and suffix behind it.
        return ' '.join(split_list[:-2]), split_list[-2], split_list[-1]

    # String 1st to (n - 1)th item as entire given name. Return family name behind it. None means no suffix.
    return ' '.join(split_list[:-1]), split_list[-1], None


def decompose_names(columns=DF_COLS_LIST):  # Argument columns can be list or string.
    decomposed_df = pd.DataFrame(names_df['names'].apply(split_name).tolist(), columns=DF_COLS_LIST)
    return decomposed_df[columns].drop_duplicates()  # Return unique data frame or series.


if __name__ == '__main__':
    print(decompose_names())
