#deployment
import joblib
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

#Save model
best_model = RandomForestClassifier(random_state=42)
best_model.fit(X_train, y_train)
model=best_model
joblib.dump(model,'model.pkl')
['model.pkl']
#the flask app
#imports
st.title('Fraud Detection App')
#Input fields
st.subheader('Enter transaction details')
#assuming 4 features
f1=st.number_input('',value=0.0)
f2=st.number_input('',value=0.0)
f3=st.number_input('',value=0.0)
f4=st.number_input('',value=0.0)

#predict button
if st.button('Predict Fraud'):
    features=np.array([[f1,f2,f3,f4]])
    prob=model.predict_proba(features)[0][1]
    if prob>0.7:
         st.error(f'Fraud Alert! Probability:{prob:.2%}')
    else:
         st.succes(f'Transaction Safe. Probability:{prob:.2f}')
