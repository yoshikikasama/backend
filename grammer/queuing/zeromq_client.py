import zmp

context = zmp.Context()
sock = context.socket(zmp.PULL)
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print(f'Received:{message.decode()}')
