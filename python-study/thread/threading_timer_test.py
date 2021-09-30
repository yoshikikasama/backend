from threading import Timer, active_count
import time


class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)

        # joinの導入
        self.thread.start()
        self.thread.join()

    def start(self):
        self.thread.start()


def printer():
    print(1)
    print(2)
    print(3)
    print(4)
    # 現在のthread数
    print("active:", active_count())
    time.sleep(5)


t = perpetualTimer(1, printer)
t.start()
print('in')
time.sleep(10)
print('OK')
