import streamlit as st
import numpy as np
import pickle

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="🔐",
    layout="centered"
)

# ── Load models ───────────────────────────────────────────────────────────────
@st.cache_resource
def load_models():
    with open("rf_model.pkl", "rb") as f:
        rf = pickle.load(f)
    with open("xgb_model.pkl", "rb") as f:
        xgb = pickle.load(f)
    return rf, xgb

rf_model, xgb_model = load_models()

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🔐 Fraud Detection App")
st.markdown(
    "Enter transaction details below and choose a model to predict whether "
    "the transaction is **fraudulent** or **legitimate**."
)
st.divider()

# ── Model selector ────────────────────────────────────────────────────────────
model_choice = st.radio(
    "Select Model",
    ["Random Forest", "XGBoost"],
    horizontal=True
)

st.divider()

# ── Input form ────────────────────────────────────────────────────────────────
st.subheader("📋 Transaction Details")

col1, col2 = st.columns(2)

with col1:
    Transaction_Amount       = st.number_input("Transaction Amount ($)", min_value=0.0, step=1.0)
    Account_Balance          = st.number_input("Account Balance ($)", min_value=0.0, step=1.0)
    Daily_Transaction_Count  = st.number_input("Daily Transaction Count", min_value=0, step=1)
    Avg_Transaction_Amount_7d= st.number_input("Avg Transaction Amount – 7d ($)", min_value=0.0)
    Failed_Transaction_Count_7d = st.number_input("Failed Transactions – 7d", min_value=0, step=1)
    Risk_Score               = st.slider("Risk Score", 0.0, 1.0, 0.5, step=0.01)
    Card_Age                 = st.number_input("Card Age (months)", min_value=0, step=1)
    Transaction_Distance     = st.number_input("Transaction Distance (km)", min_value=0.0)

with col2:
    IP_Address_Flag             = st.selectbox("IP Address Flagged?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Previous_Fraudulent_Activity= st.selectbox("Previous Fraudulent Activity?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Is_Weekend                  = st.selectbox("Is Weekend?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Transaction_Type            = st.selectbox("Transaction Type", ["POS", "Online", "ATM Withdrawal", "Bank Transfer"])
    Device_Type                 = st.selectbox("Device Type", ["Mobile", "Laptop", "Tablet"])
    Merchant_Category           = st.selectbox("Merchant Category", ["Clothing", "Electronics", "Travel", "Restaurants"])
    Card_Type                   = st.selectbox("Card Type", ["Visa", "Mastercard", "Amex"])
    Authentication_Method       = st.selectbox("Authentication Method", ["OTP", "Biometric", "Password"])

# ── Encoding ─────────────────────────────────────────────────────────────────
def encode_inputs():
    transaction_type_map   = {"POS": 2, "Online": 1, "ATM Withdrawal": 0, "Bank Transfer": 3}
    device_type_map        = {"Mobile": 1, "Laptop": 0, "Tablet": 2}
    merchant_map           = {"Clothing": 0, "Electronics": 1, "Travel": 3, "Restaurants": 2}
    card_map               = {"Visa": 2, "Mastercard": 1, "Amex": 0}
    auth_map               = {"OTP": 2, "Biometric": 0, "Password": 1}

    return np.array([[
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
    ]])

# ── Prediction ────────────────────────────────────────────────────────────────
st.divider()
if st.button("🔍 Predict", use_container_width=True, type="primary"):
    input_data = encode_inputs()
    model      = rf_model if model_choice == "Random Forest" else xgb_model

    prediction   = model.predict(input_data)[0]
    probability  = model.predict_proba(input_data)[0][1]

    st.subheader("🧾 Result")
    if prediction == 1:
        st.error(f"🚨 **Fraudulent Transaction Detected!**  \nFraud probability: **{probability:.1%}**")
    else:
        st.success(f"✅ **Transaction is Legitimate.**  \nFraud probability: **{probability:.1%}**")

    # Probability bar
    st.progress(float(probability), text=f"Fraud risk: {probability:.1%}")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Fraud Detection Project · Powered by Random Forest & XGBoost · Built with Streamlit")
