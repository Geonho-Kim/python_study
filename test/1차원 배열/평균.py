N = int(input())
n_list = list(map(int, input().split()))
max_num = max(n_list)
avg = 0
for i in range(N):
    avg += n_list[i] / max_num * 100
print(avg/N)