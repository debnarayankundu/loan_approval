import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

# Load the classifier from a pickle file
with open("classifier1.pkl", "rb") as pickle_in:
    classifier1 = pickle.load(pickle_in)

def convert_to_numeric(value):
    try:
        return float(value)  # Attempt to convert to float
    except ValueError:
        return None  # Return None if conversion fails

def predict_note_authentication(features):
    # Convert features to floats where necessary
    features = [convert_to_numeric(x) if i not in {1, 2} else x for i, x in enumerate(features)]
    prediction = classifier1.predict([features])
    return prediction[0]

def main():
    st.title("Check for Loan Approval")
    
    Name = st.text_input("Enter your name")  # Name currently not used in predictions
    
    no_of_dependents = st.text_input("Enter number of dependents")
    education = st.radio("Education", ["Graduate", "Non-Graduate"])
    education = 1 if education == "Graduate" else 0

    self_employed = st.radio("Self-Employed", ["Yes", "No"])
    self_employed = 0 if self_employed == "Yes" else 1

    income_annum = st.text_input("Enter annual income")
    loan_amount = st.text_input("Enter loan amount")
    loan_term = st.text_input("Enter loan term")
    cibil_score = st.text_input("Enter your CIBIL score")
    residential_assets_value = st.text_input("Enter total value of your residential assets")
    commercial_assets_value = st.text_input("Enter total value of your commercial assets")
    luxury_assets_value = st.text_input("Enter total value of your luxury assets")
    bank_assets_value = st.text_input("Enter total value of your bank assets")
    
    if st.button("Check Loan Status"):
        features = [
            no_of_dependents, education, self_employed, income_annum, loan_amount,
            loan_term, cibil_score, residential_assets_value, commercial_assets_value,
            luxury_assets_value, bank_assets_value
        ]

        if None not in features:  # Check if all inputs are valid
            loan_status = predict_note_authentication(features)
            result = "Rejected" if loan_status == 1 else "Approved"
            st.success(f"The loan is {result}")
        else:
            st.error("Please ensure all inputs are numeric where required and properly filled.")

if __name__ == '__main__':
    main()
