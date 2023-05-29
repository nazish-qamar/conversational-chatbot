import os
import sys
from dataclasses import dataclass
from torch.utils.data import Dataset
from transformers import GPT2Tokenizer
from src.exception import CustomException
from src.logger import logging


@dataclass
class EncoderConfig:
    tokenizer_model_file_path: str = os.path.join("artifacts", "modified_tokenizer")


class DataEncoder(Dataset):
    def __init__(self, train_data):
        self.encoder_config = EncoderConfig()
        self.train_data = None
        self.train_data = train_data
        logging.info("Inside encoder.")
        #load tokenizer
        try:
            tokenizer = GPT2Tokenizer.from_pretrained(self.encoder_config.tokenizer_model_file_path)
            self.X_encoded = tokenizer(self.train_data, max_length= 40, truncation=True, padding="max_length", return_tensors="pt")
            self.input_ids = self.X_encoded['input_ids']
            self.attention_mask = self.X_encoded['attention_mask']

        except Exception as e:
            raise CustomException(e, sys)

    def __len__(self):
        return len(self.train_data)


    def __getitem__(self, idx):
        return (self.input_ids[idx], self.attention_mask[idx])
