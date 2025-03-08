# FRAUD DETECTION PROJECT

## PROJECT OVERVIEW
* Fraudulent activities pose significant financial and reputational risks to businesses, necessiating the development of robust fraud detection systems.
* The project **aims to build a data-driven fraud detection model** that can identify suspicious transactions with high accuracy as machine learning and statistical techniques.
## BUSINESS UNDERSTANDING
* Fraud can manifest in diverse ways such as:- **unauthorised transactions,identity theft,account takeovers, and payment fraud.**
- Detecting fraudulent transactions is critical for preventing financial losses,maintaining regulatory compliance and ensuring customer trust.
- The key stakeholders for the project could include:- **Business Executives and Decision-Makers,Fraud Prevention and Risk Management Teams,Customer Support Teams,Compliance and Legal Teams,Customers and many more**
## DATA UNDERSTANDING AND PREPARATION
* The data was sourced from **[Kaggle](https://www.kaggle.com/datasets/samayashar/fraud-detection-transactions-dataset/data)**
* It contains various variables that help in fraud detection such as:
    - Transaction Details: Transaction_ID, Transaction_Amount, Transaction_Type, Timestamp.
	- User Behavior: Daily_Transaction_Count, Avg_Transaction_Amount_7d, Failed_Transaction_Count_7d.
	- Security & Risk Indicators: IP_Address_Flag, Previous_Fraudulent_Activity, Risk_Score, Authentication_Method.
	- Fraud Label: Fraud_Label (1 for fraud, 0 for genuine).

* The data was prepared by:
   - Handling Outliers in the Transaction_Amount column
   - Correcting the data type for Timestamp column
  
## VISUALIZATIONS AND ANALYSIS
* **Target Variable Analysis**
  ![image](https://github.com/user-attachments/assets/f7dfd6b6-c2ae-4c4e-ad8f-2864d35b17b1)

* **Univariate Analsis**
* **Bivariate Analysis**
* **Multivariate Analysis**
  

## MODELLING AND EVALUATION
* The data was prepared for modeling by
   - **Dropped irrelevant** columns
   - **Encoded** categorical columns
   - Defined **features and target variable**
   - Split  data into **80% for training** and **20% for testing**
   - **Standardized numerical** Features
* The models used were
  * **XGBoost,Random Forest and Logistic Regression.**
## **CONCLUSIONS**
**1**. **Fraudulent Transactions are Significant**
   -
   * **32.13%** of transactions are fraudulent,highlighting a critical need for fraud detection

**2**.**Key Fraud Indicators:**
   -
   * **Higher risk scores** are strongly correlated with fraud.
   * **Failed Transactions** and **High daily transactions** are also strong predictors.

**3**.**Model Perfomance**
   -
   * **XGBoost(96.2% accuaracy)** is the best perfoming model,effectively balancing precision and recall.
   * **Random Forest(96.4% accuracy)** is also highly effective but less optimal.
   * **Logistic Regression(78.5% accuracy** struggles due to the complexity of fraud patterns
## **RECOMMENDATIONS**
**1**. **Deploy XGBoost for Real-Time Fraud Detection**
   -
   * Since XGBoost achieves *high precision recall of 94%* , it effectively detects fraudulent transactions with minimal false negatives.
   * It should be integrated into the fraud monitering system for real-time flagging

**2**. **Enhance Risk-based Authentication**
   -
   * Transactions with **high risk scores** should trigger **additional authentication**(e.g OTP verification or biometric verifcation)
   * Users with multiple **failed transactions in a short time** should be flagged for review.

**3**. **Monitor High-Frequency Transactions**
   -
   * Accounts with **unusual daily transaction counts** should be flagged for further review.
   * Implement automated alerts for sudden spikes in transaction activity

**4**. **Regular Model Updates**
   -
   * Fraud patterns evolve, so the model should be **retarained periodically** with fresh data.
   * Incorporate **new fraud indicators** as they emerge.

## DEPLOYMENT
