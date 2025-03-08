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
  
![image](https://github.com/user-attachments/assets/15cff7f1-008e-4977-80fc-dac9130ae119) 
* 67.87% of transactions are Legitimate while 32.13% are fraudulent-indicating a moderately imbalanced dataset, meaning fraud detection models need to be optimized to handle class imbalance effectively.
* **Univariate Analysis**
  
  ![image](https://github.com/user-attachments/assets/13624f97-9599-4149-a9f8-fe927a3631af)
  * The risk score follows a uniform distribution, spread between 0.0001 and the median risk score is 0.50 indicating an even spread of risklevels.
  * Higher risk scores might be correlated with fraudulent transactions.
    
* **Bivariate Analysis**
  
  ![image](https://github.com/user-attachments/assets/3663daa3-48a5-442d-a0f9-fc06de635a68)
  * Fraudulent transactions have higher average risk scores(0.66) compared to legitimate ones(0.42).
  * The boxplot confirms that frauds tend to have higher risk scores, making it a strong predictor of fraud.
    
* **Multivariate Analysis**
  
  ![image](https://github.com/user-attachments/assets/83661528-9963-4d59-a743-034c878cac7b)
  * Risk Score and Fraud Label - 0.49 correlation-confirming that higher risk scores are strongly asscociated with fraudulent transcations.**Risk Score is likely to be a key predictor in fraud detection models.**
  * Failed Transactions and Fraud Label - 0.41 correlation thus a higher number of failed transcations correlates wth fraudulet behaviour.Fraudsters may attempt multiple failed transactions before succeding.
  * Daily Transaction Count and Fraud Label - 0.36 correlation
Accounts with more transactions are more likely to be fraudulent.

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
