from dataclasses import dataclass
from pathlib import Path

import streamlit as st
from Main import APP_TITLE
from src.datasource import get_data_pandas_example
from src.helper import get_file_header, render_markdown_file
from streamlit_pandas_profiling import st_profile_report


@dataclass
class Datasource:
  name: str = ""
  url: str = ""
  doc: str = ""
  type: str = ""
  sep: str = ","
  header: int = 0


# TODO: Load datasource info from .toml?

datasource = Datasource(name="White wine quality", type="CSV", sep=";")
datasource.url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
datasource.doc = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names"
datasource.header = 0

# TODO: Create sidebar

tab1, tab2, tab3 = st.tabs(["Dataset", "Profile", "Metadata"])

df, profile_report = get_data_pandas_example(datasource.url, datasource.sep, datasource.header)

with tab1:
  st.write(f"Data source: {datasource.name} - file header:")
  st.code(get_file_header(datasource.url))
  st.write(datasource.url)
  st.dataframe(df)
 
  
with tab2:
  st_profile_report(profile_report)

with tab3:
  render_markdown_file(Path.cwd()/"docs/pandas_example_white_wine.md")
