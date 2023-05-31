#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_encoder import DataEncoder
from src.components.model_trainer import ModelTrainer
from src.components.tokenizer_model import TokenizerModel
from src.pipeline.train_pipeline import TrainPipeline


if __name__ == "__main__":
    training_obj = TrainPipeline()
    training_obj.call_train_workflow()
