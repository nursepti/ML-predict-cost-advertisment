import numpy as np
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Create endpoint /predict-advertising
@app.route('/predict-advertising', methods=['POST', 'GET'])
def predict():
    # get argument parameter from endpoint
    data = request.args

    with open("regression.pkl", 'rb') as file:
      pk_model = pickle.load(file)

    # Predict with regression model
    prediction = pk_model.predict([[np.array(eval(data['sales']))]])
    # Get first index
    print(prediction)
    # output = {'advertising': prediction[0][0]}
    # Return prediction result
    return f"Prediksinya adalah: {prediction[0][0]}"
    # return jsonify(output)

# Run endpoint server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
