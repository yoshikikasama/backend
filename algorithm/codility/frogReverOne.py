# N : 異なる整数の個数
# A : 配列
# X以上の値のkey値を返却する


A = [2, 2, 2, 2, 2]
X = 2

def solution(X, A):
    count = 0
    leaf_set = set()
    for i in A:
        leaf_set.add(i)
        if len(leaf_set) == X:
            return count
        count += 1
    return -1

sol = solution(X, A)
print(sol)