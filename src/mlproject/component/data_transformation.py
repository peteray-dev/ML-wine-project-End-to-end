# import os
from mlproject.logging import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mlproject.config.configuration import DataTransformationConfig
import pandas as pd
import os
import joblib




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        # Load data
        data = pd.read_csv(self.config.data_path)

        # Split into train and test sets
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        # Identify the features and target
        features = [col for col in data.columns if col != 'quality']
        # target = 'quality'

        # Initialize StandardScaler
        scaler = StandardScaler()

        # Scale the features in the train and test sets
        train[features] = scaler.fit_transform(train[features])
        test[features] = scaler.transform(test[features])

        joblib.dump(scaler, os.path.join(self.config.root_dir, 'scaler.joblib'))


        # Save the scaled train and test sets
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        # Logging
        logger.info("Split into training and test sets, with scaling applied.")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        # Print the shapes (optional)
        print(f"Train shape: {train.shape}")
        print(f"Test shape: {test.shape}")

