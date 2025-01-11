import numpy as np
import pandas as pd
import streamlit as st

st.title("Sample App")

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)
