import os
import sys
from source.logger import logging
from source.exception import CustomException
import pandas as pd

from source.components.data_ingestion import DataIngestion

from source.components.data_transformation import DataTransformation
from source.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)