import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

from dataclasses import dataclass

@dataclass
class TokenizerModelConfig:
    tokenizer_path = os.path.join("artifacts", "modified_tokenizer")


class TokenizerModel:
    def __init__(self):
        self.model_trainer_config = TokenizerModelConfig()

    def initiate_tokenizer_model(self):
        tokenizer=GPT2Tokenizer.from_pretrained("gpt2")
        tokenizer.add_special_tokens({
            "pad_token": "<pad>",
            "bos_token": "<startofstring>",
            "eos_token": "<endofstring>"
        })
        tokenizer.add_tokens(["<bot>:"])
        self.save_tokenizer(tokenizer)

    def save_tokenizer(self, tokenizer):
        tokenizer.save_pretrained(self.model_trainer_config.tokenizer_path)