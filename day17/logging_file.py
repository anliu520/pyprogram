#Author:Anliu

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

#-----------------------------------

handler = logging.FileHandler("log2.txt")
handler.setLevel(level= logging.INFO)

formatter = logging.FileHandler('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(console)




try:
    mun1 = input(">>>:")
    mun2 = input(">>>:")
    conut = int(mun1) / int(mun2)
    print(conut)
    open("log1.txt","rb")
except ZeroDivisionError:
    logger.error("")
    logger.error("finash....")

logger.info("This is a info ....")
logger.error("This is a error...")
