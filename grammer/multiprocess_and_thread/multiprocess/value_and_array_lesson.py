import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def f(num, arr):
    logging.debug(num)
    num.value += 1
    logging.debug(arr)
    for i in range(len(arr)):
        arr[i] *= 2

if __name__ == '__main__':
    num = multiprocessing.Value('f', 0.0)
    arr = multiprocessing.Array('i', [1, 2 ,3 ,4 ,5])

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()
    p2 = multiprocessing.Process(target=f, args=(num, arr))
    p2.start()
    p2.join()
    logging.debug(num.value)
    logging.debug(arr[:])