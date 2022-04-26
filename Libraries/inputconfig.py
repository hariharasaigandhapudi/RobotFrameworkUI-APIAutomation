import os
from robot.api import logger
import csv

def get_input_from_csv(csv_file):
    MYDIR = os.path.dirname(__file__)
    logger.info(MYDIR)
    path = os.path.join(MYDIR, csv_file+".csv")
    logger.info(path)
    with open(path, 'r') as csvfile:
        di= dict(filter(None,csv.reader(csvfile)))
    return di