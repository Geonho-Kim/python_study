N = int(input())

for i in range(N):
    str1 = input()
    score = 0
    sum_score = 0
    for j in str1:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)
