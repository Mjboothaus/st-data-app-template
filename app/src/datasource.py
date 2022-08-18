import pandas as pd
from streamlit import cache
from pandas_profiling import profile_report

CSV_URL_EXAMPLE = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

# @cache
def get_data_pandas_example(datasource=CSV_URL_EXAMPLE, sep=",", header=0):
    try:
        df = pd.read_csv(datasource, sep=sep, header=header)
        return df, df.profile_report()
    except Exception as e:
        raise(e)

