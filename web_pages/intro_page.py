import streamlit as st
from configs.pages_config import INTRO_WIDTH_LIST, INTRO_TITLE, WEB_INTRO, SELF_INTRO, MEDIA, MEDIA_DICT


def enter_intro_page():
    """
    Set up introduction page of web application.

    It creates a container and divides it into 3 columns: self_intro_col, web_intro_col, and media_col.

    Each column is filled with relevant content: self intro, web intro, and media links.
    """
    container = st.container()
    self_intro_col, web_intro_col, media_col = st.columns(INTRO_WIDTH_LIST)
    container.title(INTRO_TITLE)

    web_intro_col.subheader(WEB_INTRO)
    web_intro_col.markdown('For me, life is about explorations 🔭')
    web_intro_col.markdown('Never know if never try. This idea propels me 🤘')
    web_intro_col.markdown('Also, as a data scientist, I am quite interested in text generation 🔡')
    web_intro_col.markdown('Thus, I come up with names creation 🎨')
    web_intro_col.markdown('BTW, sometimes unideal creations may appear 🤣')
    web_intro_col.markdown('When it happens, please just create again and see if what you desire arrives 🙏')
    web_intro_col.markdown('Hope you all can find names you like 😄')
    web_intro_col.markdown("And I'd love to hear your feedbacks on GitHub 🤝")

    self_intro_col.subheader(SELF_INTRO)
    self_intro_col.markdown('Leisure in life enjoyment 🍷')
    self_intro_col.markdown('Days in data science 💻')

    media_col.subheader(MEDIA)
    for media in MEDIA_DICT.keys():
        media_col.link_button(MEDIA_DICT[media]['icon'], MEDIA_DICT[media]['link'])
