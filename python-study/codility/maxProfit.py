A = [23171, 21011, 21123, 21366, 21013, 21367]


def solution(A):
    n = len(A)
    A.reverse()
    max = 0
    profit = 0
    tmp_profit = 0
    for k in range(n):
        max = A[k]
        for j in range(k, n-k):
            tmp_profit = max - A[j]
            if tmp_profit > profit:
                profit = tmp_profit
    return profit


sol = solution(A)
print(sol)
