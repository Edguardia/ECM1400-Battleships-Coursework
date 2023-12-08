"""prepares logging and sets configuration"""
import logging

logger = logging
logger.basicConfig(filename="battleships.log",format='%(asctime)s - %(message)s', level=logging.DEBUG)
