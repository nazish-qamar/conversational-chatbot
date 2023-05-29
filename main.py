#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_encoder import DataEncoder
from src.components.model_trainer import ModelTrainer
from src.components.tokenizer_model import TokenizerModel


if __name__ == "__main__":
    obj = DataIngestion()
    data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_set = data_transformation.initiate_data_transformation(data_path)
    tokenizer_len = TokenizerModel().initiate_tokenizer_model()
    chatData = DataEncoder(train_set)
    model = ModelTrainer()
    model.initiate_model_trainer(tokenizer_len)
    model.train(chatData)

    while True:
        inp = input()
        print(model.infer(inp))