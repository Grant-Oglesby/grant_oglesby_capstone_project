import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Streamlit Main",
    page_icon=":wave:",
    layout="wide"
)

# Sidebar setup for navigation
st.sidebar.success("Navigation")


st.title("Streamlit Main Page")

st.write("Welcome to the Streamlit app!")
