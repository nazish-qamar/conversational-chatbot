import os
import sys
import torch
from dataclasses import dataclass
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.optim import Adam
from torch.utils.data import DataLoader
from src.exception import CustomException
from src.logger import logging
import tqdm

from src.utils import process_output, infer_tokenizer_len


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model_state.pt")
    tokenizer_model_file_path: str = os.path.join("artifacts", "modified_tokenizer")


class ModelTrainer:
    def __init__(self):
        self.optim = None
        self.model_trainer_config = ModelTrainerConfig()
        self.train_data = None
        self.tokenizer_len = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None

    def initiate_model_trainer(self, tokenizer_len):
        logging.info("Inside model trainer.")
        self.tokenizer_len = tokenizer_len

        try:
            self.model = GPT2LMHeadModel.from_pretrained("gpt2")
            # need to resize as we modified the tokenizer
            self.model.resize_token_embeddings(self.tokenizer_len)
            self.model = self.model.to(self.device)
            print(self.device)
            self.model.train()
            self.optim = Adam(self.model.parameters(), lr=1e-3)
            logging.info("Leaving model trainer.")
        except Exception as e:
            raise CustomException(e, sys)

    def train(self, chatData, epochs=10):
        logging.info("Inside ModelTrainer:train.")
        if not os.path.isfile(self.model_trainer_config.trained_model_file_path):
            chatData = DataLoader(chatData, batch_size=64)
            for i in tqdm.tqdm(range(epochs)):
                for X, a in chatData:
                    X = X.to(self.device)
                    a = a.to(self.device)
                    self.optim.zero_grad()
                    loss = self.model(X, attention_mask=a, labels=X).loss
                    loss.backward()
                    self.optim.step()
                torch.save(self.model.state_dict(), self.model_trainer_config.trained_model_file_path)
        else:
            self.model.load_state_dict(torch.load(self.model_trainer_config.trained_model_file_path))

    def infer(self, inp):
        if self.model is None:
            self.model = GPT2LMHeadModel.from_pretrained("gpt2")
            # need to resize as we modified the tokenizer
            self.model.resize_token_embeddings(
                infer_tokenizer_len(self.model_trainer_config.tokenizer_model_file_path)
            )
            self.model.load_state_dict(torch.load(self.model_trainer_config.trained_model_file_path))
            # if device changed after training, use-
            # self.model.load_state_dict(torch.load(self.model_trainer_config.trained_model_file_path,
            #                                      map_location=torch.device('cpu')))
        tokenizer = GPT2Tokenizer.from_pretrained(self.model_trainer_config.tokenizer_model_file_path)
        inp = "<startofstring>"+inp+" bot: "
        inp = tokenizer(inp, return_tensors="pt")
        X = inp["input_ids"].to(self.device)
        a = inp["attention_mask"].to(self.device)
        output = self.model.generate(X, attention_mask=a, pad_token_id=tokenizer.eos_token_id, max_length=20)
        output = tokenizer.decode(output[0])

        return process_output(output)
