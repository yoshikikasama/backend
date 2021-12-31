# N 整数の数
# A 配列　
# 順列(ソートができる)であるかどうかをreturn
# 1なら順列、そうでなければ0を返す

def solution(A):
    print(len(A))
    max = 0
    tmp_list = []
    for i in A:
        if max < i:
            max = i
        tmp_list.append(i)
    if max == len(tmp_list):
        return 1
    else:
        return 0


# A = [4, 1, 3, 2]
A = [4, 1, 3]

sol = solution(A)
print(sol)