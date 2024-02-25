import asyncio
# 非同期処理
# loopのobjectを作成
loop = asyncio.get_event_loop()

async def worker():
    print('start')
    # 非同期用のコルーチンのsleep
    # yield from asyncio.sleep(2)
    # 処理を待たずに次の処理が走れる
    await asyncio.sleep(2)
    print('stop')


if __name__ == '__main__':
    # 終わるまで待つ
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()