# N 整数の数
# A 配列　
# 0は東、1は西に走る車


A = [0, 1, 0, 1, 1]

def solution(A):
    A.reverse()
    sum = 0
    suffixSum = 0
    for a in A:
        if a == 1:
            suffixSum += 1
        if a == 0:
            sum += suffixSum

    if sum > 1000000000:
        return -1
    else:
        return sum

sol = solution(A)
print(sol)