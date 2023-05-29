import sys
import os
import numpy as np
import pandas as pd
from datasets import load_from_disk

from src.exception import CustomException
from src.logger import logging
from src.utils import extract_dialogs, add_tokens_to_dialogs


class DataTransformation():
    def __init__(self):
        self.train_path: str = ""

    def initiate_data_transformation(self, train_path):
        self.train_path = train_path
        try:
            dataset = load_from_disk(train_path)
            logging.info("Read dataset from the disk completed.")
            dialog_list = extract_dialogs(dataset)
            logging.info("Dialogs extracted from the dataset.")
            padded_dialogs = add_tokens_to_dialogs(dialog_list)
            logging.info("Tokens added to the dataset.")
            return padded_dialogs
        except Exception as e:
            raise CustomException(e, sys)