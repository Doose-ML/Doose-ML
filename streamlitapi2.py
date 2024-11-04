import numpy as np
import streamlit as st
import joblib

# Load model
model = joblib.load("water project.pkl")

st.title('Water Quality Prediction')


# Get user input
ph = st.number_input('pH')
Hardness = st.number_input('Hardness')
Solids = st.number_input('Solids')
Chloramines = st.number_input('Chloramines')
Sulfate = st.number_input('Sulfate')
Conductivity = st.number_input('Conductivity')
Organic_carbon = st.number_input('Organic Carbon')
Trihalomethanes = st.number_input('Trihalomethanes')
Turbidity = st.number_input('Turbidity')



# Make prediction
input_data = np.array([[ph,Hardness, Solids, Chloramines, Sulfate, Conductivity,Organic_carbon,Trihalomethanes, Turbidity]])
prediction = model.predict(input_data)

# Show prediction
if st.button('prediction'):
    input_data = np.array([[ph,Hardness, Solids, Chloramines, Sulfate, Conductivity,Organic_carbon,Trihalomethanes, Turbidity]])
    prediction = model.predict(input_data)
    if prediction[0] ==1:
        st.write(f"Predicted water quality: {'portable'}")
    if prediction[0] ==0:
        st.write(f"Predicted water quality: {'not portable'}")