# 529

# 1024 512 256 128 64 32 16 8 4 2 1
#       1      0       0   0    0    1  0  0 0 1

# def solution(n)
# 最長の0の数のあるlengthを返す

def solution(N):
    # Nを2進数に変換
    binary_list = [2048,1024, 512, 256, 128, 64, 32 ,16, 8, 4, 2, 1]
    n_binary_list = []
    for b in binary_list:
        print(b)
        if b <= N:
            N = N - b
            n_binary_list.append(1)
        else:
            n_binary_list.append(0)
    print(n_binary_list)
    isCalc = False
    calc_gap = 0
    return_gap = 0
    for r in n_binary_list:
        if r == 0:
            if isCalc:
                calc_gap += 1
        else:
            if isCalc:
                if return_gap < calc_gap:
                    return_gap = calc_gap
                isCalc = False
            else:
                isCalc = True
    return return_gap

# print(solution(529))
print(solution(1041))

print(str(bin(529)))