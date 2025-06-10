#deployment
import joblib
import pickle 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

#Save model
best_model = RandomForestClassifier(random_state=42)
best_model.fit(X_train, y_train)

model=best_model
joblib.dump(model,'model.pkl')

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔐 Fraud Detection App")
st.write("Enter transaction details to predict if it's fraudulent.")

# Numeric Inputs
Transaction_Amount = st.number_input("Transaction Amount", min_value=0.0, step=1.0)
Account_Balance = st.number_input("Account Balance", min_value=0.0, step=1.0)
IP_Address_Flag = st.selectbox("IP Address Flag", [0, 1])
Previous_Fraudulent_Activity = st.selectbox("Previous Fraudulent Activity", [0, 1])
Daily_Transaction_Count = st.number_input("Daily Transaction Count", min_value=0)
Avg_Transaction_Amount_7d = st.number_input("Avg Transaction Amount (7d)", min_value=0.0)
Failed_Transaction_Count_7d = st.number_input("Failed Transaction Count (7d)", min_value=0)
Card_Age = st.number_input("Card Age (days)", min_value=0)
Transaction_Distance = st.number_input("Transaction Distance (km)", min_value=0.0)
Risk_Score = st.slider("Risk Score", 0.0, 1.0, 0.5)
Is_Weekend = st.selectbox("Is Weekend?", [0, 1])

# Encoded Categorical Fields
Transaction_Type = st.selectbox("Transaction Type", ["POS", "Online", "ATM Withdrawal", "Bank Transfer"])
Device_Type = st.selectbox("Device Type", ["Mobile", "Laptop", "Tablet"])
Merchant_Category = st.selectbox("Merchant Category", ["Clothing", "Electronics", "Travel", "Restaurants"])
Card_Type = st.selectbox("Card Type", ["Visa", "Mastercard", "Amex"])
Authentication_Method = st.selectbox("Authentication Method", ["OTP", "Biometric", "Password"])

# Encoding categorical fields manually
def encode_inputs():
    transaction_type_map = {"POS": 0, "Online": 1, "ATM Withdrawal": 2, "Bank Transfer": 3}
    device_type_map = {"Mobile": 0, "Laptop": 1, "Tablet": 2}
    merchant_map = {"Clothing": 0, "Electronics": 1, "Travel": 2, "Restaurants": 3}
    card_map = {"Visa": 0, "Mastercard": 1, "Amex": 2}
    auth_map = {"OTP": 0, "Biometric": 1, "Password": 2}

    return [
        Transaction_Amount,
        Account_Balance,
        IP_Address_Flag,
        Previous_Fraudulent_Activity,
        Daily_Transaction_Count,
        Avg_Transaction_Amount_7d,
        Failed_Transaction_Count_7d,
        Card_Age,
        Transaction_Distance,
        Risk_Score,
        Is_Weekend,
        transaction_type_map[Transaction_Type],
        device_type_map[Device_Type],
        merchant_map[Merchant_Category],
        card_map[Card_Type],
        auth_map[Authentication_Method],
    ]

# Predict button
if st.button("Predict"):
    input_data = np.array(encode_inputs()).reshape(1, -1)
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")