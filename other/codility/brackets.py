
S = "{[()()]}"


def solution(S):
    stack_list = []
    for i in range(len(S)):
        if S[i] == ")":
            if len(stack_list) == 0:
                return 0
            c = stack_list.pop()
            if c == "(":
                continue
            else:
                return 0
        elif S[i] == "]":
            if len(stack_list) == 0:
                return 0
            c = stack_list.pop()
            if c == "[":
                continue
            else:
                return 0
        elif S[i] == "}":
            if len(stack_list) == 0:
                return 0
            c = stack_list.pop()
            if c == "{":
                continue
            else:
                return 0
        else:
            stack_list.append(S[i])
    if len(stack_list) == 0:
        return 1
    else:
        return 0


sol = solution(S)
print(sol)
