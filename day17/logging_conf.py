#Author:Anliu
#Author:Anliu
import logging.config
#d读取日志配置文件内容
logging.config.fileConfig('logging.conf')

#创建一个日志器logger
logger = logging.getLogger("")

#日志输出内容
logger.debug("debug message.")
logger.info("info message.")
logger.warning("warning message.")
logger.error("error message.")
logger.critical("critical message.")