# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].


A = [10, 2, 5, 1, 8, 20]

def solution(A):
    sorted_A = sorted(A)
    print(sorted_A)
    for i in range(1,len(sorted_A)-1):
        print(i)
        print(sorted_A[i], sorted_A[i-1], sorted_A[i+1])
        if sorted_A[i] + sorted_A[i-1] > sorted_A[i+1]:
            return 1

    return 0


sol = solution(A)
print(sol)