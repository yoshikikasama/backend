import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def worker1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

# def worker1(d, lock):
#     logging.debug('start')
#     # lockがreleaseされるまで他の処理をできなくする
#     # lock.acquire()
#     with lock:
#         i = d['x']
#         time.sleep(5)
#         d['x'] = i + 1
#         with lock:
#             i = d['x']
#             d['x'] = i + 1
#             logging.debug(d)

# def worker2(d, lock):
#     logging.debug('start')
#     lock.acquire()
#     i = d['x']
#     d['x'] = i + 1
#     logging.debug(d)
#     lock.release()
#     logging.debug('end')




if __name__ == '__main__':
    d = {"x": 0}
    # semaphoreでlockを取得できる数を指定できる
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker2, args=(semaphore,))
    t3 = threading.Thread(target=worker3, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()

    
    
    # Rlockで2度ロックできる
    # lock = threading.RLock()
    # t1 = threading.Thread(target=worker1, args=(d, lock))
    # t2 = threading.Thread(target=worker2, args=(d, lock))
    # t1.start()
    # t2.start()
    # t = threading.Timer(3, worker2, args=(100,), kwargs={'y': 200})
    # t.start()
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     # t = threading.Thread(name='rename_worker1', target=worker1)
    #     # defaultではsetDaemonがFalseでjoinと同じ働きをする
    #     # 処理が終わった場合、t1の処理が終わっていない場合でも強制終了する
    #     t.setDaemon(True)
    #     t.start()
    
    # # t2 = threading.Thread(target=worker2, args=(100,), kwargs={'y': 200})
    # for thread in threading.enumerate():
    #     if thread is threading.currentThread():
    #         continue
    #     thread.join()
    # print('started')