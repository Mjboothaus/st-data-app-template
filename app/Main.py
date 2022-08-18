# Main.py -- for creating a basic multi-page Streamlit app

import os
from pathlib import Path

import streamlit as st

from config import settings
from src.helper import render_markdown_file

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
    test_env_var = os.environ[ENV_VAR]
except Exception:
    test_env_var = settings.ENV_VAR
    st.info("Running locally the environment variable is not available using value from `.env_dockerfile.toml,`")


st.write(f"Test environment variable: {ENV_VAR} = {test_env_var}")


render_markdown_file(Path.cwd()/"docs/Main.md")
