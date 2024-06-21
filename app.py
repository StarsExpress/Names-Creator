from configs.app_config import WEB_NAME, ICON, LAYOUT, LIGHT_THEME_CSS
from configs.pages_config import PAGES_DICT, MENU_ICON
from utils.preprocessing import prepare_image_body
from web_pages.creation_page import enter_creation_page
from web_pages.intro_page import enter_intro_page
import streamlit as st
from streamlit_option_menu import option_menu


class App:
    """
    Set up and execute web application.

    Methods:
    __init__(): set up the page configuration and prepare background image.

    execute(): execute web application, including theme and menu options.
    """

    def __init__(self):
        """
        Initialize App class: set up page configuration and prepares background image.
        """
        st.set_page_config(page_title=WEB_NAME, page_icon=ICON, layout=LAYOUT)

        background_image_body = prepare_image_body()
        st.markdown(background_image_body, unsafe_allow_html=True)

    @staticmethod
    def execute():
        """
        Apply theme and menu options to execute web application.
        Also determine which page to display based on selected menu option.
        """
        st.markdown(LIGHT_THEME_CSS, unsafe_allow_html=True)

        options = [PAGES_DICT["creation"]["name"], PAGES_DICT["intro"]["name"]]
        icons = [PAGES_DICT["creation"]["icon"], PAGES_DICT["intro"]["icon"]]

        with st.sidebar:
            selected_page = option_menu(
                "Menu",
                options,
                menu_icon=MENU_ICON,
                icons=icons,
                styles="icon",
            )

        if selected_page == PAGES_DICT["creation"]["name"]:
            enter_creation_page()
        if selected_page == PAGES_DICT["intro"]["name"]:
            enter_intro_page()
