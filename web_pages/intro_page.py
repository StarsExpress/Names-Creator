from configs.app_config import INTRO_COLS_WIDTH_LIST, INTRO_TITLE, WEB_INTRO
from configs.app_config import SELF_INTRO, MEDIA, MEDIA_DICT
import streamlit as st


def enter_intro_page():
    container = st.container()
    web_intro_col, self_intro_col, media_col = st.columns(INTRO_COLS_WIDTH_LIST)
    container.title(INTRO_TITLE)

    web_intro_col.subheader(WEB_INTRO)
    web_intro_col.markdown('Always eager to try new things.')
    web_intro_col.markdown('But be careful, sometimes unideal creations may appear XD')

    self_intro_col.subheader(SELF_INTRO)
    self_intro_col.markdown('Just a naughty man interested in data science.')

    media_col.subheader(MEDIA)
    media_col.link_button(MEDIA_DICT['instagram']['icon'], MEDIA_DICT['instagram']['link'])
    media_col.link_button(MEDIA_DICT['linkedin']['icon'], MEDIA_DICT['linkedin']['link'])
