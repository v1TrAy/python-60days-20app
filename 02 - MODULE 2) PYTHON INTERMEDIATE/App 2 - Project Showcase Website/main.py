import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=450)

with col2:
    content = """
    Back in the game, fingers flying across the keyboard like old times.
Reigniting the spark, one line of code at a time.
    """
    st.title("v1TrAy")
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content)
