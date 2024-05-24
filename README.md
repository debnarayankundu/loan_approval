# Loan Eligibility Prediction

This project aims to predict whether an individual is eligible for a loan based on various personal and financial information using a machine learning model.

## Introduction
Loan eligibility prediction is an important task for financial institutions to minimize risk and ensure responsible lending. This project leverages machine learning to predict loan eligibility based on several key features such as CIBIL score, bank assets, loan amount, and more.



## Features
The dataset includes the following features:
- `CIBIL Score`: Credit score of the individual
- `Bank Assets`: Total assets in the bank
- `Loan Amount`: Amount of loan requested
- `Residential Assets`: Value of residential property owned
- `Education`: Education level of the individual
- `Loan Term`: Duration of the loan in months/years
- `Income`: Monthly or annual income
- `Employment Status`: Employment status of the individual
- `Age`: Age of the individual
- `Marital Status`: Marital status of the individual
- `Loan History`: Previous loan repayment history
- `Outcome`: Loan eligibility status (0 or 1)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/loan-eligibility-prediction.git
    cd loan-eligibility-prediction
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Prepare the dataset:
    - Collect the dataset and ensure it includes the necessary features.
    - Place the dataset file (e.g., `loan_data.csv`) in the `data/` directory.

2. Run the data preprocessing and training script:
    ```sh
    python train_model.py
    ```

3. Evaluate the model:
    ```sh
    python evaluate_model.py

To go to the website you can  click the link: https://loanapproval-y5je5nhnc5zztsmnv7isy7.streamlit.app/



![image](https://github.com/debnarayankundu/loan_approval/assets/159264658/e19928bd-6292-427c-a9b6-02ac022b33ae)

![image](https://github.com/debnarayankundu/loan_approval/assets/159264658/640b1bfe-5d0d-4652-a5cd-2ec37e7a9a47)

