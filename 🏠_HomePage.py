import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

# set page name
st.set_page_config( page_title="AI MedCheck", )



# set title
st.image("./bckgrd_image/omdena_banner_1.png")
st.title('Welcome To Omdena 2024 Hackathon')

st.header("AI MedCheck: AI-Powered Healthcare Solutions")

st.markdown("---")

st.markdown( """ 
            <div style="background-color:#f5f5f5; padding:10px; border-radius:5px;"> 
                <p>Around the world, healthcare systems face immense challenges:</p> 
                <ul> 
                    <li><b>Limited access to specialists:</b> Many regions lack adequate access to specialized medical professionals, leading to delayed diagnoses and treatment.</li> 
                    <li><b>Growing demand for mental health support:</b> The need for mental health services is increasing, but resources are often stretched thin.</li> 
                    <li><b>Rising healthcare costs:</b> The cost of healthcare continues to rise, making it inaccessible for many individuals and families.</li> 
                </ul> 
                <p>AI has the potential to revolutionize healthcare by:</p> 
                <ul> 
                    <li><b>Improving diagnostic accuracy and speed:</b> AI algorithms can analyze medical images and data with high precision, aiding in faster and more accurate diagnoses.</li> 
                    <li><b>Enhancing treatment planning and personalization:</b> AI can help tailor treatment plans to individual patients based on their unique characteristics and needs.</li> 
                    <li><b>Increasing efficiency and reducing costs:</b> AI can automate tasks, streamline workflows, and optimize resource allocation, leading to cost savings.</li> 
                    <li><b>Expanding access to care:</b> AI-powered tools can provide remote diagnoses, monitoring, and support, making healthcare more accessible to underserved populations.</li> 
                </ul> 
            </div> """, unsafe_allow_html=True, )  
st.write()
st.write("Being said, we decided to leverage AI to improve healthcare services. We have developed the following AI-powered solutions to address key healthcare challenges:")

############################################# Lung Disease Classification #############################################
st.subheader("Lung Disease Classification")

st.markdown(
    """
    <div style="background-color:#f5f5f5; padding:10px; border-radius:5px;">
        Our advanced AI model analyzes chest X-rays to assist in the detection of
        various lung diseases, including bacterial pneumonia, viral pneumonia, corona virus, tuberculosis. It ouputs normal if no disease is detected.
        This tool aids in early diagnosis and facilitates timely medical intervention.
    </div>
    """,
    unsafe_allow_html=True, 
)

st.markdown("---")

############################################# Brain Disease Classification #############################################
st.subheader("Brain Disease Classification")

st.markdown(
    """
    <div style="background-color:#f5f5f5; padding:10px; border-radius:5px;">
        This model utilizes cutting-edge image recognition techniques to identify
        potential abnormalities in brain scans. By analyzing MRI images, it can assist
        in the detection of conditions such as glioma, menigioma, and piuitary tumors,
        enabling faster diagnosis and treatment planning. It ouputs normal if no disease is detected.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

############################################# Mental Health LLM #############################################
st.subheader("Mental Health LLM")

st.markdown(
    """
    <div style="background-color:#f5f5f5; padding:10px; border-radius:5px;">
        Our large language model provides empathetic and supportive conversations,
        offering a safe space for individuals to discuss their mental health concerns.
        It can offer coping strategies, resources, and personalized guidance to
        promote mental well-being.
    </div>
    """,
    unsafe_allow_html=True,
)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/WENDGOUNDI/" target="_blank">Savadogo Abdoul</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
