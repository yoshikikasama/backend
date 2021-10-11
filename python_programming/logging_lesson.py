import logging

import log_test
logging.basicConfig(filename='test.log', level=logging.INFO)


# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logger.setLevel(logging.DEBUG)
logging.info('info')

log_test.do_something()
