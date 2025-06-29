import time
import threading


def worker():
    print(time.time())


def scheduler(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
            print('in')
            print(threading.active_count())
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)


scheduler(1, worker)
