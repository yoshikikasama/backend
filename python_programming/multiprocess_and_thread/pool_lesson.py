import multiprocessing
import logging
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    return i


if __name__ == '__main__':
    # pool:同時にrunするthreadの数を指定できる
    with multiprocessing.Pool(1) as p:
        # 最初に同期処理を行う方法
        logging.debug(p.apply(worker1, (200, )))
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100, )) 
        logging.debug('executed')
        logging.debug(p1.get())
        logging.debug(p2.get())
