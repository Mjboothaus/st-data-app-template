# Main.py -- for creating a basic multi-page Streamlit app

import os
from pathlib import Path
from config import settings
from src.helper import render_markdown_file, show_dir_tree

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

ENV_VAR = "API_KEY"

try:
    st.write(f"Test container environment variable: {ENV_VAR} = {os.environ[ENV_VAR]}")
except Exception as e:
    st.info("If running locally the environment variable is not available - see package which caters for this.")
    #
    # st.write(e)


render_markdown_file(Path.cwd()/"docs/Main.md")

tree = show_dir_tree(Path.cwd(), not_hidden=False)