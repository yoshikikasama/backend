# X = 10 現在地点
# Y = 85　この地点以上にいきたい
# D = 30　カエルの一回のジャンプの距離数

# Y地点以上いくためのカエルのジャンプ回数をreturnする

# def solution(X, Y, D):
#     count = 0
#     flag_run = X
#     while True:
#         if flag_run < Y:
#             flag_run += D
#             count += 1
#         else:
#             return count 


def solution(X, Y, D):
    diff = Y - X
    print(diff)
    return -(-diff//D)

X = 10
Y = 85
D = 30

sol = solution(X, Y, D)
print(sol)
