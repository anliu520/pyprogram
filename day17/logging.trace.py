#Author:Anliu

import logging
#from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
#rHandler = RotatingFileHandler("log.txt",maxBytes = 1*1024,backupCount = 3)
#rHandler.setLevel(logging.INFO)

handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#rHandler.setFormatter(formatter)
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
#console.setFormatter(formatter)

#logger.addHandler(rHandler)
logger.addHandler(handler)
logger.addHandler(console)

logger.info("this is a test from info")
logger.debug("This is a test from debug")
logger.warning("This is a test from warning")
logger.info("Finish")

try:
    open("sklearn.txt","rb")
except (SystemExit,KeyboardInterrupt):
    raise
except Exception:
    logger.error("Faild to open sklearn.txt from logger.error",exc_info = True)

logger.info("Finish")
