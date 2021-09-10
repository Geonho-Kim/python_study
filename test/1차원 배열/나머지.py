n_list = []
for i in range(10):
    num = int(input())
    n_list.append(num%42)
n_list = set(n_list)
print(len(n_list))
