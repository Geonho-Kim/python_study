T = int(input())

for i in range(T):
    R, S = input().split()
    S_len = len(S)
    S = list(map(str, S))
    for j in S:
        for k in range(S_len):
            print(j, end="")
