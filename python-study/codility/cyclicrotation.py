# N個の整数
# 配列A
# K　シフト数
# 1 63897
# 2 76389
# 3 97638
def solution(A, K):
    for _ in range(K):
        for i in range(len(A)):
            if i+1 == len(A):
                tmp = A.pop(i)
                A.insert(0, tmp)
    return A

a = [0, 0, 0]
k = 1

sol = solution(a, k)
print(sol)