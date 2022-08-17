import streamlit as st

from Main import APP_TITLE

st.write("Page 1")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
  st.write(f"{APP_TITLE} - Tab 1")
  
  
with tab2:
  st.write(f"{APP_TITLE} - Tab 2")
