A = [-3, 1, 2, -2, 5, 6]
# A = [10, 10, 10]
# A = [-5, 5, -5, 4]

def solution(A):
    A.sort()
    print(A)
    max1 = A[-1] * A[-2] * A[-3]
    max2 = A[0] * A[1] * A[-1]

    if max1 > max2:
        return max1
    else:
        return max2
    
    # # 最大値を3つ導き出す
    # sorted_list = sorted(A, reverse=True)
    # print(sorted_list)
    # max_list = sorted_list[:3]
    # print(max_list)
    # sum = 1
    # # 3つの最大値を掛け算したものをreturn
    # for j in max_list:
    #     sum *= j
    # return sum

sol = solution(A)
print(sol)