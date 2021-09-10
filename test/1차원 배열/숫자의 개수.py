A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))   # ['1', '7', '0', '3', '7', '3', '0', '0']
for i in range(10):
    print(result.count(str(i)))
