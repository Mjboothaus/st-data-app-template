from pathlib import Path

import streamlit as st
from Main import APP_TITLE
from src.sidebar import create_sidebar_utilities
from seedir import seedir

ITEM_LIMIT=50

def create_page_0_tab_0():
    my_path = Path.cwd().as_posix()
    exclude_folders = [folder.parts[-1] for folder in Path(my_path).iterdir() if folder.is_dir() and "venv" in folder.as_posix()]
    exclude_folders.append(".git")
    dir_str = seedir(path=my_path, style='emoji', sort=True,
                     printout=False, itemlimit=ITEM_LIMIT, depthlimit=depth, 
                     exclude_folders=exclude_folders)
    st.code(f"Excluding: {', '.join(exclude_folders)}")
    st.code(dir_str)


depth = create_sidebar_utilities()

TAB_NAMES = ["Directory structure", "Tab 2"]
tab0, tab1 = st.tabs(TAB_NAMES)

with tab0:
    create_page_0_tab_0()


with tab1:
    st.write(f"{APP_TITLE}: {TAB_NAMES[1]}")
