import streamlit as st
from helpers import Cloud_Predictor
st.title("CloudI Demo")
st.header("Name clouds with CloudI!")
reminder = "Please upload your image below"
user_inputImage = st.file_uploader(label = reminder)
if user_inputImage is not None:
    from PIL import Image
    imageDisplay = Image.open(user_inputImage).convert("RGB")
    st.image(imageDisplay, caption = "Your clouds", 
    use_column_width = 'auto')
    scores, prediction, des_dir = Cloud_Predictor(imageDisplay)
    st.title(prediction)
    description = open(des_dir, "r")
    description_text = description.read()
    st.text("With prediction probability: " + "{:.3f}".format(scores))
    st.markdown(description_text)
    st.markdown("*Definition Source*: [WMO](https://cloudatlas.wmo.int/zh-hans/descriptions-of-clouds.html)")



