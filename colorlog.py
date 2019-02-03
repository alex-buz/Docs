import colorlog

logger = colorlog.getLogger()  1
logger.setLevel(colorlog.colorlog.logging.DEBUG)  2

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())  3
logger.addHandler(handler)

logger.debug("Debug message")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
