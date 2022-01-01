
# A = [3, 4, 3, 2, 3, -1, 3, 3]
A = [6, 8, 4, 6, 8, 6, 6]
# A = [1, 2, 3, 4, 5, 6, 7]


# 配列の中で過半数を占める数字を返却する
def slowLeader(A):
    n = len(A)
    leader = -1
    for k in range(n):
        candidate = A[k]
        print(candidate)
        # candidateが配列の中に何個含まれているかをcount
        count = 0
        for i in range(n):
            if (A[i] == candidate):
                count += 1
        print(count, n, n//2)
        # 過半数以上かどうかを判断している
        if (count > n // 2):
            leader = candidate
    return leader


sol = slowLeader(A)
print(sol)