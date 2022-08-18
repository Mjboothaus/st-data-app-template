# Main.py -- for creating a basic multi-page Streamlit app

import os
from pathlib import Path
from config import settings
from src.helper import render_markdown_file

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
    st.write(os.environ["API_KEY"])
except Exception as e:
    st.write(e)


render_markdown_file(Path.cwd()/"docs/Main.md")
