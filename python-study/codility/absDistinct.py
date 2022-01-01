A = [-5, -3, -1, 0, 3, 6]

def solution(A):
    absolute_distinct_list = []
    for i in A:
        if 0 > i:
            i = -i
        if not i in absolute_distinct_list:
            absolute_distinct_list.append(i)
    return len(absolute_distinct_list)


sol = solution(A)
print(sol)