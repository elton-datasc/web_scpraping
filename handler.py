import logging
from logging import FileHandler, StreamHandler
from logging import INFO

logging.basicConfig( 
    level=logging.INFO,
    encoding = 'utf-8', 
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[FileHandler("logs.txt", "a"), StreamHandler()]
)