
def solution(A, B, K):
    count = 0
    for i in range(A, B+1):
        if i % 2 == 0:
            count += 1
    return count 



A = 6
B = 11
K = 2

sol = solution(A, B, K)
print(sol)