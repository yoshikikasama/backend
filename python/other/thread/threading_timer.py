from threading import Timer, active_count


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
        print(active_count())

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def printer():
    print('test')
    # 現在のthread数


t = perpetualTimer(1, printer)
t.start()
print('in')
