import streamlit as st

def create_sidebar_main():
    st.sidebar.header("Sidebar Main Header")


def create_sidebar_utilities():
    return st.sidebar.slider("Directory tree: Level depth", min_value=1, max_value=5, value=3, step=1)