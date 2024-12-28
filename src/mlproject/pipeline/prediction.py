import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        self.scaler = joblib.load(Path('artifacts/data_transformation/scaler.joblib'))

    def predict(self, data):
        if not isinstance(data, pd.DataFrame):
            input_data = pd.DataFrame([input_data])

        # Scale features
        features = self.scaler.transform(input_data)

        # Predict
        predictions = self.model.predict(features)

        return predictions