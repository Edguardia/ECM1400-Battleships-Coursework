"""prepares logging and sets configuration"""
import logging
import yaml

with open("config.yaml", "r", encoding='utf-8') as file:
    config = yaml.safe_load(file)

logger = logging
logger.basicConfig(filename="battleships.log",format='%(asctime)s - %(message)s',
                   level=config['logging_level'])
