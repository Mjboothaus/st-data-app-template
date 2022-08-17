import streamlit as st

st.write("Page 1")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
  st.write("Tab 1")
  
  
with tab2:
  st.write("Tab 2")
