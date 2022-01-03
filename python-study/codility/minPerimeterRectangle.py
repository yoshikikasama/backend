# 整数N = 30
# A * Bであり、周囲は2 * (A + B)

N = 30

def solution(N):
    count_list = []
    for i in range(1, N):
        if N % i == 0:
            quotient = N//i
            remainder = i
            count_list.append(2 * (quotient + remainder))
    return min(count_list)
            
sol = solution(N)
print(sol)

