import contextlib


def is_ok_job():
    try:
        print('do something')
        return True
    except Exception:
        return False


def cleanup():
    print('clean up')


try:
    is_ok = is_ok_job()
    print('more task')
finally:
    if not is_ok:
        cleanup()
