#Author:Anliu


'''
handle all the logging works
'''
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


import logging
from conf import settings

def logger(log_type):

    #create logger
    logger = logging.getLogger(log_type)
    #print(logger)
    logger.setLevel(settings.LOG_LEVEL)


    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = "%s/log/%s" %(settings.BASE_DIR,settings.LOG_TYPES[log_type])
    #print(log_file)
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    #print(logger)
    return logger
    # 'application' code
'''
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
'''

logger("access")
