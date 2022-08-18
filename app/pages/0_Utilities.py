from pathlib import Path

import streamlit as st
from Main import APP_TITLE
from src.dirtree import show_dir_tree


TAB_NAMES = ["Directory structure", "Tab 2"]


tab0, tab1 = st.tabs(TAB_NAMES)

with tab0:
  st.write(f"{APP_TITLE}: {TAB_NAMES[0]}")
  
  with st.spinner("Creating directory tree"):
    tree = show_dir_tree(Path.cwd(), not_hidden=False)

  
with tab1:
  st.write(f"{APP_TITLE}: {TAB_NAMES[1]}")
