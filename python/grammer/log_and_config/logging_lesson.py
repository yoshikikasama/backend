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

# logging.StreamHandler ⇨ コンソール出力
# logging.FileHandler ⇨ ファイル出力


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('filter test')
logger.info('password')

logging.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})
