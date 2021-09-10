N = int(input())
num = input().split()
for i in range(N):
    num[i] = int(num[i])
print(min(num), end=' ')
print(max(num))
