from threading import Timer


class RepeatedTimer(Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        Timer.__init__(self, interval, self.run, args, kwargs)
        self.thread = None
        self.function = function

    def run(self):
        self.thread = Timer(self.interval, self.run)
        self.thread.start()
        self.function(*self.args, **self.kwargs)

    def cancel(self):
        if self.thread is not None:
            self.thread.cancel()
            self.thread.join()
            del self.thread


if __name__ == '__main__':

    import time

    def hello(message):
        hello.counter += 1
        print(message, hello.counter)
    hello.counter = 0

    t = RepeatedTimer(0.5, hello, ["Hello"])
    t.start()
    time.sleep(5)
    t.cancel()
    print("Done.")
