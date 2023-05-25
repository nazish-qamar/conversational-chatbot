from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    obj = DataIngestion()
    data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_list = data_transformation.initiate_data_transformation(data_path)