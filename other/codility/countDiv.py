def solution(A, B, K):
    count = 0
    for i in range(A, B+1):
        if i % K == 0:
            count += 1
    return count 


# A = 6
# B = 11
# K = 2
A = 11
B = 345
K = 17

# expect 20
sol = solution(A, B, K)
print(sol)
