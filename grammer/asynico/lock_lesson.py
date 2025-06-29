import asyncio

loop = asyncio.get_event_loop()

async def worker1(lock):
    print('worker1 start')
    with await lock:
        print('worker1 got lock')
        await asyncio.sleep(3)
    print('worker1 end')

@asyncio.coroutine
def worker2(lock):
    print('worker2 start')
    with (yield from lock):
        print('worker2 got lock')
        yield from asyncio.sleep(3)
    print('worker2 end')


lock = asyncio.Lock()
loop.run_until_complete(asyncio.wait([
    worker1(lock),
    worker2(lock)
]))