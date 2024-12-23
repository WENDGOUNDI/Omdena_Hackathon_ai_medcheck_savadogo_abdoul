# Libraries Importation
import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import predLung_Disease, set_background


set_background('./bckgrd_image/lung_bckgrd.jpg')

# set title
st.title('AI MedCheck: Lung Disease Classification')

# set header
st.header('Please upload a Lung X-ray image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
#model = load_model('./model/pneumonia_classifier.h5')
# Load the model
model_path = "./trained_models/lung_model.h5"

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    resized_image = image.resize((224, 224))
    st.image(resized_image)

    # classify image
    class_name, conf_score = predLung_Disease(image, model_path)

    # write classification
    #st.write("## {}".format(class_name))
    st.write("### Prediction: {}".format(class_name))
    #st.write("### score: {}%".format(int(conf_score * 1000) / 10))
