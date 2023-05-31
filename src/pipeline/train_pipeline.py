import sys

from src.components.data_encoder import DataEncoder
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.tokenizer_model import TokenizerModel
from src.exception import CustomException
from src.read_configuration import Configurations


class TrainPipeline:
    def __init__(self):
        pass

    def call_train_workflow(self):
        try:
            token_config = Configurations().read_config()
            obj = DataIngestion()
            data_path = obj.initiate_data_ingestion()
            data_transformation = DataTransformation(token_config)
            train_set = data_transformation.initiate_data_transformation(data_path)
            tokenizer_len = TokenizerModel(token_config).initiate_tokenizer_model()
            chatData = DataEncoder(train_set)
            model = ModelTrainer()
            model.initiate_model_trainer(tokenizer_len)
            model.train(chatData)

            while True:
                inp = input()
                print(model.infer(inp))

        except Exception as e:
            raise CustomException(e, sys)