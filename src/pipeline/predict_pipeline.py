import sys

from src.components.model_trainer import ModelTrainer
from src.exception import CustomException


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, user_input):
        try:
            model = ModelTrainer()
            return model.infer(user_input)

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, input: str):
        self.input = input

    def get_data(self):
        try:
            custom_data_input_dict = {
                "input": [self.input]
            }
            return custom_data_input_dict

        except Exception as e:
            raise CustomException(e, sys)
