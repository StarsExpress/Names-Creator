from configs.app_config import NO_BORDERS_CSS
from configs.pages_config import CREATION_WIDTH_LIST, CREATION_TITLE, CREATION_HEADER, SLIDER, MIN_NUM, MAX_NUM
from configs.pages_config import GENDER, PREFERENCE, GENDER_DICT, PREFERENCE_DICT, EXPANDER, DETAILS
from configs.pages_config import BUTTON, SPINNER, CHAT_NAME, CHAT_AVATAR, METRIC, METRIC_DICT
from utils.composition import make_creations
import streamlit as st


def enter_creation_page():
    st.markdown(NO_BORDERS_CSS, unsafe_allow_html=True)  # Make sure the form has no borders at all.

    with st.form('names_creation', clear_on_submit=True):
        container = st.container()
        creations_col, gender_col, preference_col, metrics_col = st.columns(CREATION_WIDTH_LIST)

        container.title(CREATION_TITLE)
        container.header(CREATION_HEADER)

        creations_col.subheader(SLIDER)
        names_number = creations_col.slider('Number of Names', min_value=MIN_NUM, max_value=MAX_NUM,
                                            label_visibility='hidden')
        gender_col.subheader(GENDER)
        gender = gender_col.radio('Gender', GENDER_DICT.keys(), label_visibility='hidden')

        preference_col.subheader(PREFERENCE)
        preference = preference_col.radio('Preference', PREFERENCE_DICT.keys(), label_visibility='hidden')

        with preference_col:  # Write expander inside options column.
            with st.expander(EXPANDER):
                st.write(DETAILS)

        total_runtime, avg_runtime = 0, 0  # Default is 0.

        if preference_col.form_submit_button(BUTTON):
            with creations_col:  # Write spinner and created names inside creations column.
                with st.spinner(SPINNER):
                    names_list, total_runtime, avg_runtime = make_creations(names_number, GENDER_DICT[gender],
                                                                            PREFERENCE_DICT[preference])

                names_col, download_col = st.columns([CREATION_WIDTH_LIST[0] * 0.67, CREATION_WIDTH_LIST[0] * 0.33])
                with names_col:
                    with st.chat_message(CHAT_NAME, avatar=CHAT_AVATAR):
                        for name in names_list:
                            st.write(name)

        metrics_col.subheader(METRIC)
        metrics_col.metric(METRIC_DICT['total'], f'{str(total_runtime)} s')
        metrics_col.metric(METRIC_DICT['avg'], f'{str(avg_runtime)} s')
