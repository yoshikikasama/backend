# def memoize(f):
#     memo = {}

#     def _wrapper(n):
#         if n not in memo:
#             # function実行
#             memo[n] = f(n)
#             print('hit')
#             print(memo)
#         return memo[n]
    # return _wrapper


# @memoize
import functools
# 何度も値を取得するようなapiの結果を保持するときなどに使用する


@functools.lru_cache(maxsize=5)
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in range(10):
    print(long_func(i))

print(long_func.cache_info())
print('next run')
for i in range(10):
    print(long_func(i))

print(long_func.cache_info())
long_func.cache_clear()
