import logging

from training import Training
from helper import create_validation_file_from_train_file
from helper import write_first_n_lines_of_file

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(message)s',
                    datefmt="%H:%M:%S")

logging.getLogger('bert-classifier')
