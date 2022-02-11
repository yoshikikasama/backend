import contextlib


def is_ok_job():
    try:
        print('do something')
        return True
    except Exception:
        return False


def cleanup():
    print('clean up')


# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         cleanup()

with contextlib.ExitStack() as stack:
    # 最後に呼ばれる関数
    stack.callback(cleanup)

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        # stackの中身を取り出すことで最後に呼ばれないようにする
        stack.pop_all()
