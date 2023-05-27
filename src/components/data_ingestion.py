import os
import sys
import pandas as pd
from datasets import load_dataset
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', "data")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            if not os.path.isdir(self.ingestion_config.raw_data_path):
                logging.info('Read the dataset')
                dataset = load_dataset("conv_ai_2")
                os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
                dataset['train'].save_to_disk(self.ingestion_config.raw_data_path)
                logging.info("Ingestion of the data is completed")
            else:
                logging.info("Dataset already exists.")

            return (
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
