import os
import sys
from dataclasses import dataclass
from transformers import GPT2LMHeadModel
from torch.optim import Adam
from src.exception import CustomException
from src.logger import logging

#from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    tokenizer_model_file_path = os.path.join("artifacts", "modified_tokenizer")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        self.train_data = None
        self.tokenizer_len = None

    def initiate_model_trainer(self, train_data, tokenizer_len):
        logging.info("Inside model trainer.")
        self.train_data = train_data
        self.tokenizer_len = tokenizer_len

        try:
            #load tokenizer

            model = GPT2LMHeadModel.from_pretrained("gpt2")
            model.resize_token_embeddigns() #need to resize as we modified the tokenizer
            model.train()
            optim = Adam(model.parameters())
        except:
            pass
