import threading
import time


event = threading.Event()


def race():
    print("startしました。")
    event.wait()
    print("goalです。おめでとう！")


thread = threading.Thread(target=race)
thread.start()
time.sleep(1)
print("走っています")
time.sleep(1)
event.set()
