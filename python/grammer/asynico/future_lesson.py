import asyncio

loop = asyncio.get_event_loop()


async def f(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')


def got_result(future):
    print(future.result())
    loop.stop()


future = asyncio.Future()
# 確実に終わることを確認するメソッド
asyncio.ensure_future(f(future))

future.add_done_callback(got_result)

loop.run_forever()
# loop.run_until_complete(future)
# print(future.result())
loop.close()