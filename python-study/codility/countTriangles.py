# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].

A = [10, 2, 5, 1, 8, 12]


def solution(A):
    count = 0
    for p in range(len(A)):
        for q in range(p + 1, len(A)):
            for r in range(q+1, len(A)):
                if all((
                    (A[p] + A[q] > A[r]),
                    (A[q] + A[r] > A[p]),
                    (A[r] + A[p] > A[q])
                )):
                    count += 1

    return count


sol = solution(A)
print(sol)
