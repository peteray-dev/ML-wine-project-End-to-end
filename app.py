from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlproject.pipeline.prediction import PredictionPipeline

app = Flask(__name__) # initialization of flask

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/prediction',methods=['GET'])  # route to display the home page
def prediction():
    return render_template("prediction.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # print("Form Data Received:", request.form)

            # Convert form inputs to a NumPy array
            fields = [
                'fixed_acidity', 'volatile_acidity', 'citric_acid',
                'residual_sugar', 'chlorides', 'free_sulphur_dioxide',
                'total_sulphur_dioxide', 'density', 'pH', 'sulphates', 'alcohol'
            ]
            data = [float(request.form[field]) for field in fields]
            data = np.array(data).reshape(1, -1)

            # print("Processed Data:", data)

            # Prediction logic
            obj = PredictionPipeline()
            prediction = obj.predict(data)

            print("Prediction Result:", prediction)
            return render_template('result.html', prediction=str(prediction))

        except Exception as e:
            print("The Exception message is:", e)
            return f"Error during processing: {e}"
    else:
        return render_template('index.html')
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)