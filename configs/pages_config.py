"""All page configurations."""

# Menu settings.
PAGES_DICT = {'creation': {'name': "Let's Create", 'icon': 'magic'},
              'intro': {'name': 'About Me', 'icon': 'arrow-through-heart'}}
MENU_ICON = 'book'


# Creation page settings.
CREATION_WIDTH_LIST = [3, 1, 1.5, 1.1]  # Columns (creation, gender, preference, and metrics) relative widths.
CREATION_TITLE = 'Meet new people, shall we?'
CREATION_HEADER = '🔠 Logits ⛲ stream and 🔢 letters are 🎇 lit'

# Slider, radio and expander.
SLIDER = '💡 Number of Creations'
MAX_NUM = 50
MIN_NUM = 1

GENDER = '👫 Gender'
PREFERENCE = '😀 Preference'
GENDER_DICT = {'🚺 Female': 'female', '🚹 Male': 'male'}
PREFERENCE_DICT = {'🆕 Forename Only': 'just_forename', '🌈 Remix Full Name': 'remix',
                   '🆕 Surname Only': 'just_surname', '🆕 Full Name': 'full_name'}

EXPANDER = "📌 What's remix?"  # Explain preference definitions.
DETAILS = 'New forename combined with existing surname.'

# Button, spinner and metric.
BUTTON = '🧪 Create'
SPINNER = '🏎️ On our ways, dear 🏎️'
CHAT_NAME = 'Here you go'
CHAT_AVATAR = '🎙'

METRIC = '⏲️ Runtime'
METRIC_DICT = {'total': 'Total', 'avg': 'Average per name'}


# Intro page settings.
INTRO_WIDTH_LIST = [2.5, 4, 2]  # Columns (web intro, self intro, media) relative widths.
INTRO_TITLE = 'Feel Fun'

WEB_INTRO = "Why Names Creation"

SELF_INTRO = "About Author"

MEDIA = 'Social Media'
MEDIA_DICT = {'instagram': {'icon': '🔮 Instagram',
                            'link': "https://www.instagram.com/blackjack625/"},
              'linkedin': {'icon': '🖇️ LinkedIn',
                           'link': "https://www.linkedin.com/in/Yuan-Jack-Yao/"},
              'github': {'icon': '🐈‍⬛ Github',
                         'link': "https://github.com/StarsExpress"}}
