import streamlit as st

st.title("Sample App")

if st.button("Click me"):
    st.write("Clicked!")

if st.checkbox("Click me"):
    st.write("Clicked!")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.write(f"選択肢: {options}")

number = st.sidebar.slider("Pick a Num", 0, 100, 40)
st.sidebar.write(f"number: {number}")

left_col, right_col = st.columns(2)
left_col.slider("Pick a Num in Left", 0, 100)
right_col.slider("Pick a Num in Right", 0, 100)
