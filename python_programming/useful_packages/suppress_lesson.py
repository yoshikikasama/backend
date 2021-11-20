import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    # suppressは例外が発生してもpassする
    os.remove('somefile.tmp')