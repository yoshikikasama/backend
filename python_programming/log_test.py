import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def do_something():
    logger.info('from logetst')
    logger.debug('from logtest debug')
