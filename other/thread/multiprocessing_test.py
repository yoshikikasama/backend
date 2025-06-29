from multiprocessing import Queue, Process
import time

# 生産プロセス


def produce(queue):
    for i in range(10):
        queue.put(i)
        time.sleep(2)

# 消費プロセス


def consume(queue):
    for i in range(10):
        n = queue.get()
        print(n)
        time.sleep(2)


if __name__ == '__main__':
    queue = Queue()

    # プロセス生成
    p0 = Process(target=produce, args=(queue,))
    p1 = Process(target=produce, args=(queue,))
    c0 = Process(target=consume, args=(queue,))
    c1 = Process(target=consume, args=(queue,))

    # プロセス開始
    p0.start()
    p1.start()
    c0.start()
    c1.start()

    # プロセス終了待ち合わせ
    p0.join()
    p1.join()
    c0.join()
    c1.join()
