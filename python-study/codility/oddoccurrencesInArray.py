# N 整数の数
# A 配列　
# 対になっているが、なっていない要素が1つだけある
# 対になってない要素をreturnする

# pythonのset関数を使用すれば、簡単にできるかも

def solution(A):
    test_list = []
    for i in A:
        print(i)
        if i in test_list:
            for j in range(len(test_list)):
                print(test_list)
                if i == test_list[j]:
                    test_list.pop(j)
                    break
        else:
            test_list.append(i)
        
    return test_list[0]

A = [9, 3, 9, 3, 9, 7, 9]
sol = solution(A)
print(sol)
