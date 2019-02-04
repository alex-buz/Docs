from colorama import init, Fore, Back, Style
init(autoreset=True)

messages = [
    'blah blah blah',
    (Fore.LIGHTYELLOW_EX + Style.BRIGHT
        + BACK.MAGENTA + 'Alert!!!'),
    'blah blah blah'
]

for m in messages:
    print(m)

    
    
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
