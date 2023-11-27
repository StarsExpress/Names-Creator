"""All app configurations."""

import os

# File settings.
APP_BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project folder.

DATA_FOLDER_PATH = os.path.join(APP_BASE_PATH, 'data')  # Data folder.


# Web settings.
WEB_NAME = 'Names Creator'
ICON = '🎰'
LAYOUT = 'wide'
