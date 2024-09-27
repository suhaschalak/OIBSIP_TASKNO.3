import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Sales Prediction App")
st.write("Enter the values for TV, Radio, and Newspaper to predict sales.")

# User inputs
tv = st.number_input("TV Advertising Budget ($):", min_value=0.0)
radio = st.number_input("Radio Advertising Budget ($):", min_value=0.0)
newspaper = st.number_input("Newspaper Advertising Budget ($):", min_value=0.0)

# Make predictions
if st.button("Predict Sales"):
    input_data = pd.DataFrame({'TV': [tv], 'Radio': [radio], 'Newspaper': [newspaper]})
    predicted_sales = model.predict(input_data)
    st.success(f"Predicted Sales: ${predicted_sales[0]:.2f}")
