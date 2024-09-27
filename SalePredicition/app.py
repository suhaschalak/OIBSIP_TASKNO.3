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
    predicted_sales = model.predict(input_data)[0]

    # Show prediction result
    st.success(f"Predicted Sales: ${predicted_sales:.2f}")

    # Prepare data to save
    result_df = pd.DataFrame({
        'TV': [tv],
        'Radio': [radio],
        'Newspaper': [newspaper],
        'Predicted Sales': [predicted_sales]
    })

    # Save to CSV
    csv_file_path = 'predicted_sales.csv'
    result_df.to_csv(csv_file_path, index=False)

    # Provide download link for the CSV
    st.download_button(
        label="Download Predicted Sales as CSV",
        data=result_df.to_csv(index=False).encode('utf-8'),
        file_name=csv_file_path,
        mime='text/csv'
    )
