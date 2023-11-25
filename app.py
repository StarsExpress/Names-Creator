from configs.app_config import WEB_NAME, ICON, LAYOUT, COLS_WIDTH_LIST, PAGE_TITLE, PAGE_HEADER
from configs.app_config import SLIDER, MIN_NUMBER, MAX_NUMBER, GENDER, PREFERENCE, GENDER_DICT, PREFERENCE_DICT
from configs.app_config import EXPANDER, DETAILS, BUTTON, SPINNER, CHAT_NAME, CHAT_AVATAR, METRIC, METRIC_DICT
from utils.composition import make_creations
import streamlit as st


class App:
    """Meet creations."""

    def __init__(self):
        st.set_page_config(page_title=WEB_NAME, page_icon=ICON, layout=LAYOUT)
        self.container = st.container()
        self.creations_col, self.gender_col, self.preference_col, self.metrics_col = st.columns(COLS_WIDTH_LIST)

    def execute(self, lock):
        self.container.title(PAGE_TITLE)
        self.container.header(PAGE_HEADER)

        total_runtime, avg_runtime = 0, 0  # Total and average runtime start from 0.

        self.creations_col.subheader(SLIDER)  # Number of creations.
        number = self.creations_col.slider('Number of Names', min_value=MIN_NUMBER, max_value=MAX_NUMBER)
        self.gender_col.subheader(GENDER)
        gender = self.gender_col.radio('Gender', GENDER_DICT.keys())

        self.preference_col.subheader(PREFERENCE)
        preference = self.preference_col.radio('Preference', PREFERENCE_DICT.keys())

        with self.preference_col:  # Write expander inside options column.
            with st.expander(EXPANDER):
                st.write(DETAILS)

        if self.preference_col.button(BUTTON):
            with self.creations_col:  # Write spinner and created names inside creations column.
                with st.spinner(SPINNER):
                    names_list, total_runtime, avg_runtime = make_creations(number, lock, GENDER_DICT[gender],
                                                                            PREFERENCE_DICT[preference])

                st.chat_message(CHAT_NAME, avatar=CHAT_AVATAR)
                for name in names_list:
                    st.write(name)

        self.metrics_col.subheader(METRIC)
        self.metrics_col.metric(METRIC_DICT['total'], f'{str(total_runtime)} s')
        self.metrics_col.metric(METRIC_DICT['avg'], f'{str(avg_runtime)} s')
