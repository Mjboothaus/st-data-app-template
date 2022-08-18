from pathlib import Path

import streamlit as st
from Main import APP_TITLE
#from src.dirtree import show_dir_tree

from seedir import seedir


TAB_NAMES = ["Directory structure", "Tab 2"]


tab0, tab1 = st.tabs(TAB_NAMES)

with tab0:
    st.write(f"{APP_TITLE}: {TAB_NAMES[0]}")

    dir_str = seedir(path=Path.cwd().as_posix(), style='emoji',
                     printout=False, itemlimit=10, depthlimit=2, exclude_folders='.git')
    st.code(dir_str)


with tab1:
    st.write(f"{APP_TITLE}: {TAB_NAMES[1]}")
