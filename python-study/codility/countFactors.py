# 素数(primeNumber)：1かその数自身を除いて割り切ることができない整数
# ex: 1, 2 , 3 ,5 , 7 , 13
# 約数(divisors)： Aが他の整数Bで割り切れる時、整数Bのこと、1とそれ自身以外に割りきれる整数をもつ
# ex: 4, 6, 8, 10 
# Nの因数の数を返す
# N = 24のとき、因数は1, 2, 3, 4, 6, 8, 12, 24
# returnは8を返す
N = 24


def solution(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    return count



sol = solution(N)
print(sol)