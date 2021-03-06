import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

from PIL import Image
image_game = Image.open('image.jpg')

st.sidebar.info('This app is created using tensorflow and Streamlit')
st.sidebar.info('Abdoulaye Badji')
st.sidebar.success('https://www.youtube.com/channel/UCZ_Sor5J6415zV8k3hNlk6Q')
st.sidebar.image(image_game)

st.title("Image Classification : Paper - Rock - Scissors  ")
model = tf.keras.models.load_model("my_model.hdf5")
### load file
uploaded_file = st.file_uploader("Choose a image file (Paper or Rock or Scissors)", type=["jpg","png","JPEG"])

map_dict = {0: 'paper',
            1: 'rock',
            2: 'scissors',}


if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(150,150))
    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="RGB")

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]

    Genrate_pred = st.button("Generate Prediction")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Label for the image is {}".format(map_dict [prediction]))
        


