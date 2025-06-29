import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.FileHandler('log_test.log')
logger.addHandler(h)


def do_something():
    logger.info('from logetst')
    logger.debug('from logtest debug')
