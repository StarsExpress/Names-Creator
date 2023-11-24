"""All app configurations."""

import os

# File settings.
APP_BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Where all files are stored.


# Page settings.
WEB_NAME = 'Names Creator'
ICON = ':slot_machine:'
LAYOUT = 'wide'

COLS_WIDTH_LIST = [4, 1.5, 1.1]  # Columns (creation, preference, and metrics) relative widths.
PAGE_TITLE = 'Meet new people, shall we?'
PAGE_HEADER = ':capital_abcd: Logits :fountain: stream and :1234: letters are :sparkler: lit'


# Slider, radio and expander settings.
SLIDER = ':bulb: Number of Creations'
MAX_NUMBER = 50
MIN_NUMBER = 1

LABEL = 'hidden'  # Hide labels for slider and radio.

RADIO = ':grinning: Preference'
# Radio option emoji can't be shortcodes.
PREFERENCE_DICT = {'🆕 Forename Only': 'just_forename', '🌈 Remix Full Name': 'remix',
                   '🆕 Surname Only': 'just_surname', '🆕 Full Name': 'full_name'}

EXPANDER = ":pushpin: What's remix?"
# Explain preference definitions.
DETAILS = 'New forename combined with existing surname.'


# Button, spinner and metric settings.
BUTTON = ':test_tube: Create'
SPINNER = ':racing_car:  On our ways, dear  :racing_car:'
CHAT_NAME = 'Here you go'
CHAT_AVATAR = '🎙'  # Avatar emoji can't be shortcodes.

METRIC = ':timer_clock: Runtime'
METRIC_DICT = {'total': 'Total', 'avg': 'Average per name'}
