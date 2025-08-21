import streamlit as st
import os


# Function to display the next image in the list
def next_image():
    st.session_state.image_index = (
        st.session_state.image_index + 1
    ) % len(image_list)


# Function to display the previous image in the list
def back_image():
    st.session_state.image_index = (
        st.session_state.image_index - 1
    ) % len(image_list)


# Function to change the image index to a serious image
def serious_toggle():
    if st.session_state.serious is True:
        st.session_state.serious = False
        st.session_state.fun_or_serious = "Serious Mode"
        if st.session_state.first_fun is True:
            st.session_state.first_fun = False
            st.balloons()
    else:
        st.session_state.serious = True
        st.session_state.fun_or_serious = "Fun Button"


# Page configuration
st.set_page_config(
    page_title="Streamlit Main"
)

# Create list of images from images folder
image_list = [
    image
    for image in os.listdir(
        os.path.join(os.path.dirname(__file__), 'images')
    )
].sort()
serious_image_list = [
    image
    for image in os.listdir(
        os.path.join(os.path.dirname(__file__), 'serious_images')
    )
].sort()
text_list = [
    text
    for text in os.listdir(
        os.path.join(os.path.dirname(__file__), 'text')
    )
].sort()

# Initialize session state for image index
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0
    st.session_state.serious = True
    st.session_state.fun_or_serious = "The Fun Button"
    st.session_state.first_fun = True

# Sidebar setup for navigation
st.sidebar.title("Main Page")

# Main content
st.title("Grant Oglesby Capstone Project")
st.write(
    "An insight into the madness that is ETL pipelines "
    "with poorly reported data"
)
# Empty space for image to work with session_state and functions
with st.empty():
    # Enter image into Streamlit from images folder
    if st.session_state.serious is False:
        image_path = os.path.join(
            os.path.dirname(__file__),
            'images', image_list[st.session_state.image_index])
    else:
        image_path = os.path.join(
            os.path.dirname(__file__),
            'serious_images', serious_image_list[st.session_state.image_index])
    st.image(image_path)
# Image credits to ChatGPT
if st.session_state.serious is False:
    st.write("Credit for all stickman images goes to ChatGPT")
# Display text description
with st.expander("Notes"):
    st.markdown(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'text', text_list[st.session_state.image_index]
            )
        ).read()
    )

# Use columns for navigation buttons to present side by side
# Buttons will change the image and text being displayed
# Buttons will also disable at the end and start of the images
col1, col2, col3 = st.columns(3)
with col1:
    st.button(
        'Back',
        on_click=back_image,
        disabled=st.session_state.image_index == 0
    )
with col2:
    st.button(
        label=st.session_state.fun_or_serious,
        on_click=serious_toggle
    )
with col3:
    st.button(
        'Next',
        on_click=next_image,
        disabled=st.session_state.image_index == len(image_list) - 1
    )
