# N : 異なる整数の個数
# 1〜N+1の範囲の整数を含んでいる
# かけている要素を導き出す(この場合は4)
#テスト観点：最大値、最小値

def solution(A):
    loop = len(A) + 1
    for i in range(loop):
        i+= 1
        print(i)
        print(A)
        if not i in A:
            return i


A = [2, 3, 1, 5]

solution(A)