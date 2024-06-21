from configs.app_config import DATA_FOLDER_PATH
import os
import base64


def prepare_image_body():
    """
    Read and encode image to base64. Prepare it to be used as a background image in a style tag.

    Returns:
        str: string containing style tag with background image.
    """
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
