"""All app configurations."""

import os

# File settings.
APP_BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project folder.

DATA_FOLDER_PATH = os.path.join(APP_BASE_PATH, 'data')  # Data folder.

# Web settings.
WEB_NAME = 'Names Creator'
ICON = ':slot_machine:'
LAYOUT = 'wide'

PAGES_DICT = {'creation': {'name': "Let's Create", 'icon': 'magic'},
              'intro': {'name': 'About Me', 'icon': 'arrow-through-heart'}}
MENU_ICON = 'book'

# Creation page settings.
CREATION_COLS_WIDTH_LIST = [3, 1, 1.5, 1.1]  # Columns (creation, gender, preference, and metrics) relative widths.
CREATION_TITLE = 'Meet new people, shall we?'
CREATION_HEADER = ':capital_abcd: Logits :fountain: stream and :1234: letters are :sparkler: lit'

# Slider, radio and expander settings.
SLIDER = ':bulb: Number of Creations'
MAX_NUMBER = 50
MIN_NUMBER = 1

GENDER = ':couple: Gender'
PREFERENCE = ':grinning: Preference'
# Radio option emoji can't be shortcodes.
GENDER_DICT = {'🚺 Female': 'female', '🚹 Male': 'male'}
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

# Intro page settings.
INTRO_COLS_WIDTH_LIST = [2.5, 2.5, 2]  # Columns (web intro, self intro, media) relative widths.
INTRO_TITLE = 'Feel Fun'

WEB_INTRO = "Why Names Creation"

SELF_INTRO = "About Author"

MEDIA = 'Social Media'
MEDIA_DICT = {'instagram': {'icon': '🔮 Instagram',
                            'link': "https://www.instagram.com/blackjack625/"},
              'linkedin': {'icon': '🖇️ LinkedIn',
                           'link': "https://www.linkedin.com/in/遠姚jack/"}}
