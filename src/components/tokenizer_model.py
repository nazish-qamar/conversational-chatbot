import os
import sys
import json

from transformers import GPT2Tokenizer
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging


@dataclass
class TokenizerModelConfig:
    tokenizer_path = os.path.join("artifacts", "modified_tokenizer")


class TokenizerModel:
    def __init__(self):
        self.model_trainer_config = TokenizerModelConfig()

    def initiate_tokenizer_model(self):
        logging.info("Creating tokenization model.")
        tokenizer_len = 0
        try:
            if not os.path.isdir(self.model_trainer_config.tokenizer_path):
                tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
                tokenizer.add_special_tokens({
                    "pad_token": "<pad>",
                    "bos_token": "<startofstring>",
                    "eos_token": "<endofstring>"
                })
                tokenizer.add_tokens(["<bot>:"])
                tokenizer_len = len(tokenizer)
                self.save_tokenizer(tokenizer)
            else:
                logging.info("Skipping tokenizer processing as tokenizer already exists")
                added_tokens_file = self.model_trainer_config.tokenizer_path+"/added_tokens.json"
                with open(added_tokens_file, 'r') as f:
                    data = json.load(f)

                tokenizer_len = max(data.values()) + 1

        except Exception as e:
            raise CustomException(e, sys)

        return tokenizer_len


    def save_tokenizer(self, tokenizer):
        try:
            tokenizer.save_pretrained(self.model_trainer_config.tokenizer_path)
            logging.info("Tokenizer model saved.")
        except Exception as e:
            CustomException(e, sys)
