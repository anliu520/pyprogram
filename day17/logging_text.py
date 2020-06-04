#Author:Anliu

import logging

# debug --> info -->warning -->error --critical
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s %(name)s',datefmt='%m-%d-%Y %I:%M:%S %p',filename='example.log',level=logging.INFO)

logging.warning("usr [anliu] attempted wrong password more than 3 times")
logging.debug("usr [anliu] create file seccessful...")
logging.info("usr [anliu] tihis is  a info ...")
logging.error("usr [naliu] tihis is error ....")
logging.critical("usr [anliu]   this is a criticall ...")
