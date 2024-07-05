import streamlit as st
from configs.app_config import NO_BORDERS_CSS
from configs.pages_config import CONTAINER_TITLE, CONTAINER_HEADER, COLUMNS_WIDTH_LIST
from configs.pages_config import CREATION_SLIDER, MIN_NUM, MAX_NUM, CREATIVITY_SLIDER, CREATIVITY_DICT
from configs.pages_config import GENDER, TARGET, GENDER_DICT, TARGET_DICT, TARGET_EXPANDER, TARGET_DETAILS
from configs.pages_config import BUTTON, SPINNER, CHAT_NAME, CHAT_AVATAR, METRIC, METRIC_DICT
from utils.composition import make_creations


def enter_creation_page():
    """
    Set up creation page of web application.

    It creates a form with several input fields for user to specify parameters for name creation.

    Parameters include: number of names, creativity level, gender, and target.

    After user submits form, this function calls `make_creations` function to generate names.

    Created names are then displayed in a chat message on creation page.

    This function also calculates and displays total and average time taken to create names.
    """
    st.markdown(NO_BORDERS_CSS, unsafe_allow_html=True)

    with st.form("names_creation", clear_on_submit=True):
        container = st.container()
        container.title(CONTAINER_TITLE)
        container.header(CONTAINER_HEADER)

        # Underscores: blank columns.
        (creations_col, _, creativity_col, _,
         gender_col, _, target_col, _, metrics_col) = st.columns(COLUMNS_WIDTH_LIST)

        creations_col.subheader(CREATION_SLIDER)
        num_names = creations_col.slider(
            "Amount", min_value=MIN_NUM, max_value=MAX_NUM, label_visibility="hidden"
        )

        creativity_col.subheader(CREATIVITY_SLIDER)
        creativity = creativity_col.select_slider(
            "Creativity Level",
            options=list(CREATIVITY_DICT.keys()),
            label_visibility="hidden",
        )

        gender_col.subheader(GENDER)
        gender = gender_col.radio(
            "Gender", GENDER_DICT.keys(), label_visibility="hidden"
        )

        target_col.subheader(TARGET)
        target = target_col.radio(
            "Target", TARGET_DICT.keys(), label_visibility="hidden"
        )

        with target_col:  # Write expander inside options column.
            with st.expander(TARGET_EXPANDER):
                st.write(TARGET_DETAILS)

        total_time, avg_time = 0, 0  # Default is 0.

        if target_col.form_submit_button(BUTTON):
            with creations_col:  # Write spinner and created names inside creations column.
                with st.spinner(SPINNER):
                    names_list, total_time, avg_time = make_creations(
                        num_names,
                        CREATIVITY_DICT[creativity],
                        GENDER_DICT[gender],
                        TARGET_DICT[target],
                    )

                names_col, download_col = st.columns(
                    [COLUMNS_WIDTH_LIST[0] * 0.67, COLUMNS_WIDTH_LIST[0] * 0.33]
                )
                with names_col:
                    with st.chat_message(CHAT_NAME, avatar=CHAT_AVATAR):
                        for name in names_list:
                            st.write(name)

        metrics_col.subheader(METRIC)
        metrics_col.metric(METRIC_DICT["total"], f"{str(total_time)} s")
        metrics_col.metric(METRIC_DICT["avg"], f"{str(avg_time)} s")
