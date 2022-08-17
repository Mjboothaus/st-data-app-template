# Main.py -- for creating multipage app

import os
from pathlib import Path
from config import settings

import streamlit as st

# from helper_functions import read_render_markdown_file

APP_TITLE = settings.APP_TITLE
SUB_TITLE = settings.SUB_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide",
    menu_items={
        "About":
        "Created with love & care at DataBooth - www.databooth.com.au"
    })


def create_app_header(app_title, subtitle=None):
    st.header(app_title)
    if subtitle is not None:
        st.subheader(subtitle)
    return None


create_app_header(APP_TITLE, SUB_TITLE)

try:
    st.write(os.environment["TEST_ENV_VAR"])
except Exception as e:
    st.write(e)

# read_render_markdown_file("docs/Main.md", output="streamlit")
