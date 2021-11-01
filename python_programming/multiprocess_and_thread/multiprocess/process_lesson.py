import multiprocessing
import logging
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    time.sleep(i)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    time.sleep(i)
    logging.debug('end')


if __name__ == '__main__':
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    # t1のthreadの処理が終わっていなくても強制終了する
    t1.daemon = True
    t2 = multiprocessing.Process(name='renamed_worker2', target=worker2, args=(i,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
