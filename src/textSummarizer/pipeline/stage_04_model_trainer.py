from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.model_trainer import ModelTrainer
from textSummarizer.logging import logger
import os

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        if  os.path.exists("artifacts/model_trainer"):
            logger.info(f"model is alraedy trained>>>>>>>. Skipping training.")
        else:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config) 
            model_trainer_config.train()

            