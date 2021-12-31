# N 魚の個数
# 配列A 魚の大きさ
# 配列B 魚の方向　0は上流、1は下流

# P < Qであれば、魚Pは魚Qの上流に位置するのが初期状態
# 生きる魚の数をreturnする

def solution(A, B):
    count = 0
    # stores the 1 fish in stack
    stack_1_fish = []
    print(A)
    print(B)
    for index in range(len(A)):
        if B[index] == 0:
            # until stack has some 1 fish
            while stack_1_fish:
                # get last fish from stack and check if it can die or not
                # the larger fish eats the smaller one.
                # two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them
                if stack_1_fish[-1] > A[index]:
                    # stack 1 fish kill to current fish
                    # exit from while loop and else block also execute next top for loop
                    # check for other fish fight
                    print("Killed by " + str(stack_1_fish[-1]) + " Die " + str(A[index]))
                    break
                else:
                    # stack 1 fish is killed by current fish
                    p = stack_1_fish.pop()
                    print("Killed by " + str(A[index]) + " Die " + str(p))

            # this is the case when stack becomes empty ie. no fish of kind 1
            # it would never meet previous fish but can fight with downstream fish
            else:
                print("Count fish as remaining......." + str(A[index]))
                count += 1
        else:
            # fish 1 found add to stack
            stack_1_fish.append(A[index])
            print("1 fish found, add to stack, it can kill or killed by someone..." + str(A[index]))
            print(stack_1_fish)

    print("Count: " + str(count))
    print("Stack 1 fish: " + str(len(stack_1_fish)))
    return count + len(stack_1_fish)


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

sol = solution(A, B)
print(sol)