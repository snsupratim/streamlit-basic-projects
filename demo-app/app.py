import streamlit as st

# Configure the page and remove the navbar
st.set_page_config(page_title="Simple App", layout="wide")

# Hide Streamlit navbar and footer using custom CSS
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main app content
st.write("Hello Streamlit")

x = st.text_input("Input something -- ")
st.write(f"Your favorite movie is: {x}")
