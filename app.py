import streamlit as st
from PIL import Image as PILImage
import requests
from io import BytesIO
import main
import cv2

# Set Streamlit options
st.set_option('deprecation.showfileUploaderEncoding', False)

# Function to set dark mode or light mode
def set_theme(mode):
    if mode == 'Dark Mode':
        st.markdown("""
            <style>
            .main {
                background-color: #0e1117;
                color: #cfcfcf;
            }
            .sidebar .sidebar-content {
                background-color: #0e1117;
                color: #cfcfcf;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #cfcfcf;
            }
             .stSelectbox > div > div > div > div {
                color: #cfcfcf;
            }
            .stButton > button {
                color: #cfcfcf;
            

            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .main {
                background-color: #f0f2f6;
                color: #000000;
            }
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
                color: #000000;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #000000;
            }
            .stSelectbox > div > div > div > div {
                color: #ffffff;
            }
            .stButton > button {
                color: #ffffff;}
                label {
                color: #000000 !important;
            }
             
            </style>
            """, unsafe_allow_html=True)

# Title of the app
# Title of the app with custom styling
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    </style>
    <div class="title">Image Classification App <br> By <br> Team Ganja Ka Bhanja</div>
    """, unsafe_allow_html=True)
st.write("")

# Option for dark mode and light mode
mode = st.selectbox('Choose a theme:', ['Light Mode', 'Dark Mode'])
set_theme(mode)

# Option for user to select either upload image or enter URL
option = st.selectbox('How would you like to provide the image?', ('Upload an image', 'Enter image URL'))

uploaded_image = None

if option == 'Upload an image':
    file_up = st.file_uploader("Upload an image", type="jpeg")
    if file_up is not None:
        uploaded_image = PILImage.open(file_up)
        st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
    # Button to produce the result
    if uploaded_image and st.button("Produce Result"):
        # Call your image classification function here
        image=PILImage.open(file_up)
        result, probability = main.predict_imagefromfile(image)  # Change here
        if result == 1:
            st.write('Prediction: Real 👍')
            st.write('Probability of real image is ', probability.item())
        elif result == 0:
            st.write('Prediction: Fake 🤥')
            st.write('Probability of real image is ', probability.item())
        else:
            st.write('''Sorry No prediction can be done. File Should be stored in the same source folder.''')
            

        

elif option == 'Enter image URL':
    url = st.text_input("Enter image URL")
    response = None
    st.button("Submit URL")
    if url:
        try:
            response = requests.get(url)
            uploaded_image = PILImage.open(BytesIO(response.content))
            st.image(uploaded_image, caption='Image from URL.', use_column_width=True)
        except Exception as e:
            st.write("Invalid URL or unable to fetch the image. Please try again.")
    # Button to produce the result
    if uploaded_image and st.button("Produce Result"):
#         st.write("Just a second...")
        # Call your image classification function here
        result, probability = main.predict_image(url)
        if result == 1:
            st.write('Prediction: Real 👍')
        else:
            st.write('Prediction: Fake 🤥')
        st.write('Probability of real image is ', probability.item())


