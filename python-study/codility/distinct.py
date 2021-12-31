
A = [2, 1, 1, 2, 3, 1]


def solution(A):
    disSet = set()
    for i in A:
        disSet.add(i)
    
    return len(disSet)

sol = solution(A)
print(sol)