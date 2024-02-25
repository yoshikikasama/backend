import asyncio

loop = asyncio.get_event_loop()


def hello(name, loop):
    print(f'Hello {name}')
    loop.stop()

# 3秒後に実行
loop.call_later(3, hello, 'Mike', loop)

loop.call_soon(hello, 'Nancy', loop)
loop.run_forever()
loop.close()

