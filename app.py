#deployment
import joblib
from sklearn.ensemble import RandomForestClassifier

#Save model
model=best_model
joblib.dump(model,'model.pkl')

from flask import Flask, request, jsonify
import numpy as np

#load the model
model=joblib.load('model.pkl')

#create flask app
app=Flask(__name__)
@app.route('/predict', methods=['POST'])

def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1,-1)
    probability = model.predict_proba(features)[0][1]
    alert = 'Fraud Alert!' if probability > 0.7 else 'Transaction Safe'
    return jsonify({'fraud_probability': probability, 'alert': alert})

if __name__ == '__main__':
    app.run(debug=True)