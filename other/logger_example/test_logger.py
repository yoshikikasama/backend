from my_logger import MyLogger

my_logger = MyLogger(__name__)
logger = my_logger.logger


def ff():
    logger.info("test")


ff()

def errors():
    logger.warning('Errr')


print(errors)