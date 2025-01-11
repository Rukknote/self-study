import pandas as pd
import streamlit as st

st.title("Sample app")
df = pd.DataFrame(
    {
        "1列目": [1, 2, 3, 4],
        "2列目": [-1, -2, -3, -4],
    }
)

st.dataframe(df.style.highlight_max(axis=0))

st.json({"data": {"name": "abc", "age": 123}})
