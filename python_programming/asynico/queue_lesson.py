import asyncio
from asyncio.locks import queue

loop = asyncio.get_event_loop()

async def worker1(queue):
    with await queue:
        print('worker1 start')
        await asyncio.sleep(3)
        print('worker1 end')


async def worker2(queue):
    with await queue:
        print('worker2 start')
        await asyncio.sleep(3)
        print('worker2 end')


queue = asyncio.Queue(2)
loop.run_until_complete(asyncio.wait([
    worker1(queue),
    worker2(queue),
]))
loop.close()