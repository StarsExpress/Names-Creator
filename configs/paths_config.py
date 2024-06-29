"""All paths configurations."""

import os

# File settings.
APP_BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_FOLDER_PATH = os.path.join(APP_BASE_PATH, "data")

MODELS_FOLDER_PATH = os.path.join(APP_BASE_PATH, "models")
