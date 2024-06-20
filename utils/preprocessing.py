from configs.app_config import DATA_FOLDER_PATH
import os
import pandas as pd
import base64


def read_unique_names(name_type: str):  # Options: male_forenames, female_forenames, surnames.
    names_file_path = os.path.join(DATA_FOLDER_PATH, name_type)
    names_df = pd.read_csv(names_file_path, sep='\t', header=None, names=['names'])

    if names_df['names'].is_unique is False:
        names_df.drop_duplicates(inplace=True)
        names_df.reset_index(drop=True, inplace=True)
        names_df.to_csv(names_file_path, header=False, index=False)

    return names_df['names']  # Return series.


def prepare_image_body():
    image_path = os.path.join(DATA_FOLDER_PATH, 'background.jpg')
    image = open(image_path, 'rb')
    background_image = image.read()
    image.close()

    decoded_image = base64.b64encode(background_image).decode()
    page_image = f"""
                    <style>
                    .stApp {{
                    background-image: url("data:image/jpg;base64,{decoded_image}");
                    background-size: cover;
                    }}
                    </style>
                  """
    return page_image


def encode_names_list_to_csv(
        gender: str,
        names_list: list[str],
):
    names_df = pd.DataFrame(names_list, columns=[f'{gender.capitalize()} Names'])
    return names_df.to_csv(index=False).encode('utf-8')


def turn_names_list_to_txt(
        gender: str,
        names_list: list[str],
):
    return '\n'.join([f'{gender.capitalize()} Names'] + names_list)
