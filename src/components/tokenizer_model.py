import os
import sys

from transformers import GPT2Tokenizer
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import infer_tokenizer_len


@dataclass
class TokenizerModelConfig:
    tokenizer_path = os.path.join("artifacts", "modified_tokenizer")


class TokenizerModel:
    def __init__(self, token_config):
        self.token_config = token_config
        self.model_trainer_config = TokenizerModelConfig()

    def initiate_tokenizer_model(self):
        logging.info("Creating tokenization model.")
        tokenizer_len = 0
        try:
            if not os.path.isdir(self.model_trainer_config.tokenizer_path):
                tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
                tokenizer.add_special_tokens({
                    "pad_token": "<pad>",
                    "bos_token": self.token_config['start_token'],
                    "eos_token": self.token_config['end_token']
                })
                tokenizer.add_tokens([self.token_config['bot_token'] + ":"])
                tokenizer_len = len(tokenizer)
                self.save_tokenizer(tokenizer)
            else:
                logging.info("Skipping tokenizer processing as tokenizer already exists")
                tokenizer_len = infer_tokenizer_len(self.model_trainer_config.tokenizer_path)

        except Exception as e:
            raise CustomException(e, sys)

        return tokenizer_len

    def save_tokenizer(self, tokenizer):
        try:
            tokenizer.save_pretrained(self.model_trainer_config.tokenizer_path)
            logging.info("Tokenizer model saved.")
        except Exception as e:
            CustomException(e, sys)
