import os          # Data Ingestion Module
import sys       # System modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.exception import CustomException

from src.logger import logging    # Logging module
import pandas as pd

from sklearn.model_selection import train_test_split    # Train-test split   
from dataclasses import dataclass            # Data class for configuration

@dataclass
class DataIngestionConfig:                     # Configuration for data ingestion
    train_data_path: str = os.path.join('artifacts', 'train.csv')     ##input data path
    test_data_path: str = os.path.join('artifacts', 'test.csv')         ##output data path
    raw_data_path: str = os.path.join('artifacts', 'data.csv')          ##raw data path

class DataIngestion:                          # Data ingestion class
    def __init__(self):                   
        self.ingestion_config = DataIngestionConfig()  # Initialize config (DataIngestionConfig)

    def initiate_data_ingestion(self):       # Method to initiate data ingestion  (utils read data from CSV)
        logging.info("Entered the data Ingestion started")  # Log start of ingestion
        try:
            df = pd.read_csv('notebook/data/stud.csv')  # Read data from CSV
            logging.info("Data read successfully")  # Log successful read
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  # Create directories if not exist
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False)  # Save raw data
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  # Split data
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)  # Save train data
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)    # Save test data
            
            logging.info("Data Ingestion completed successfully")  # Log completion
            
            return(
                 self.ingestion_config.train_data_path/  
                 self.ingestion_config.test_data_path
            )  # Return paths of train and test data
        
        except Exception as e:  # Handle exceptions
            raise CustomException(e, sys)  # Raise custom exception
        
if __name__ == "__main__":
    obj = DataIngestion()  # Create an instance of DataIngestion
    obj.initiate_data_ingestion()  # Call the method to initiate data ingestion