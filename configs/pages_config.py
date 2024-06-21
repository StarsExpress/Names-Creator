"""All pages configurations."""

# Menu settings.
PAGES_DICT = {
    "creation": {"name": "Let's Create", "icon": "magic"},
    "intro": {"name": "About Me", "icon": "arrow-through-heart"},
}
MENU_ICON = "book"


# Creation page settings.
CONTAINER_TITLE = "Meet new people, shall we?"
CONTAINER_HEADER = "🔠 Logits ⛲ stream and 🔢 letters are 🎇 lit"

SPACE_WIDTH = 0.1  # Space between columns.
# Columns: creation, creativity, gender, preference, metrics.
COLUMNS_WIDTH_LIST = [
    1.8,
    SPACE_WIDTH,
    1.2,
    SPACE_WIDTH,
    1,
    SPACE_WIDTH,
    1.2,
    SPACE_WIDTH,
    0.8,
]

CREATION_SLIDER = "💡 Amount"
MAX_NUM = 30
MIN_NUM = 1

CREATIVITY_SLIDER = "🎨 Creativity"
CREATIVITY_DICT = {
    "Slight": 5,
    "Medium": 10,
    "Fancy": 15,
    "Wild": 20,
    "Limitless": None,
}

GENDER = "👫 Gender"
GENDER_DICT = {"🚺 Female": "female", "🚹 Male": "male"}

TARGET = "😀 Target"
TARGET_DICT = {
    "🆕 Forename Only": "just_forename",
    "🌈 Remix Full Name": "remix",
    "🆕 Surname Only": "just_surname",
    "🆕 Full Name": "full_name",
}

TARGET_EXPANDER = "📌 What's remix?"  # Explain preference definitions.
TARGET_DETAILS = "New forename combined with existing surname."

BUTTON = "🧪 Create"
SPINNER = "🏎️ On our ways, dear 🏎️"
CHAT_NAME = "Here you go"
CHAT_AVATAR = "🎙"

METRIC = "⏲️ Time"
METRIC_DICT = {"total": "Total", "avg": "Average per name"}


# Intro page settings.
INTRO_WIDTH_LIST = [2.5, 4, 2]  # Relative widths (web intro, self intro, media).
INTRO_TITLE = "Feel Fun"

WEB_INTRO = "Why Names Creation"
SELF_INTRO = "About Author"

MEDIA = "Social Media"
MEDIA_DICT = {
    "instagram": {
        "icon": "🔮 Instagram",
        "link": "https://www.instagram.com/blackjack625/",
    },
    "linkedin": {
        "icon": "🖇️ LinkedIn",
        "link": "https://www.linkedin.com/in/yuan-jack-yao/",
    },
    "github": {
        "icon": "🐈‍⬛ Github",
        "link": "https://github.com/StarsExpress"
    },
}
