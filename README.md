# Omdena Hackathon: AI MedCheck

This repository contains the code for an AI-powered healthcare web application designed to assist in preliminary medical assessments. The application utilizes cutting-edge AI models to provide insights into mental health, brain abnormalities, and lung diseases.

## Features

* **Mental Health Assessment:** An LLM-based chatbot interacts with users, analyzes their queries, and provides relevant mental health assessments.
* **Brain Scan Analysis:**  Utilizes advanced image recognition techniques to identify potential abnormalities in brain MRI scans, such as glioma, meningioma, and pituitary tumors. Outputs "Normal" if no disease is detected.
* **Chest X-ray Analysis:**  Analyzes chest X-rays to detect potential lung diseases, including bacterial pneumonia, viral pneumonia, coronavirus, and tuberculosis. Outputs "Normal" if no disease is detected.

## Needs Addressed

* **Accessibility:** Provides easier access to preliminary medical assessments, especially for individuals with limited access to healthcare professionals.
* **Early Detection:** Aids in the early detection of potential health issues, enabling faster intervention and treatment.
* **Efficiency:** Streamlines the diagnostic process for healthcare professionals, potentially saving time and resources.

## Benefits

* **Improved Patient Outcomes:** Early detection and faster diagnosis can lead to better treatment outcomes and improved overall health.
* **Reduced Healthcare Costs:**  Potentially reduces the cost of diagnosis by streamlining the process and enabling earlier intervention.
* **Increased Awareness:** Raises awareness about mental health and encourages individuals to seek help when needed.

## How it Works

The application is built using [insert frameworks and libraries used e.g., React, Flask, TensorFlow, PyTorch]. Each AI model has been trained on a comprehensive dataset of [describe datasets used for each model e.g., medical transcripts for the LLM, annotated brain MRI scans, and labeled chest X-rays].

## Disclaimer

This application is intended for informational purposes only and should not be used as a substitute for professional medical advice. Always consult a qualified healthcare professional for any health concerns.

## Note

This project was developed for [Omdena 2024 Hackathon] and demonstrates the potential of AI in revolutionizing healthcare.

## Getting Started

1. **Clone the repository:** `git clone https://github.com/WENDGOUNDI/Omdena_Hackathon_ai_medcheck_savadogo_abdoul.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the application:** `streamlit run 🏠_HomePage.py`

## Improvement
The system can be trained on more data to enhance its efficiency and/or more classes for better generalization.

## Inference

1. **Mental Chatbot**
   <img width="947" alt="inference_mental_chatbot" src="https://github.com/user-attachments/assets/a1ee9841-7b62-40fb-8efa-26d508f55a07" />
2. **Brain Disease Classification**
   <img width="955" alt="inference_brain_model" src="https://github.com/user-attachments/assets/1b60ed78-ce25-4300-8cd0-c8b9957296f6" />
3. **Lung Disease Classification**
 <img width="949" alt="inference_lung_model" src="https://github.com/user-attachments/assets/6a28871a-d38e-46e3-9f7e-bd47e02a9a4f" />

 ## Datasets
 1. **Lung Dataset:** https://www.kaggle.com/datasets/omkarmanohardalvi/lungs-disease-dataset-4-types
 
 2. **Brain Dataset:** https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

 3. **LLM:** We leverage prompt engineering + OpenAI chatgpt-o4-mini to assisting the users queries. The has been implemented to not answer questions out of its scope.
    <img width="951" alt="prompt_engineering" src="https://github.com/user-attachments/assets/99b737ce-5d2f-4ce5-8523-b8bc8a925a00" />
