# Libraries Importation
import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils import predBrain_Disease, set_background


set_background('./bckgrd_image/brain_bckgrd.jpg')

# set title
st.title('AI MedCheck: Brain Disease Classification')

# set header
st.header('Please upload a Brain X-ray image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# Load the model
brain_model_path = "./trained_models/brain_model.h5"
adjust_class_names = {"glioma": "Glioma", 
                      "meningioma": "Meningioma", 
                      "notumor": "No Tumor", 
                      "pituitary": "Pituitary"}

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    resized_image = image.resize((512, 512))
    st.image(resized_image)

    # classify image
    class_name, conf_score = predBrain_Disease(image, brain_model_path)
    class_name = class_name.strip()

    # write classification
    st.write("### Prediction: {}".format(adjust_class_names[class_name]))
    #st.write("### score: {}%".format(int(conf_score * 1000) / 10))
