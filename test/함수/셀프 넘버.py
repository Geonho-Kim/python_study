generated_num = set()
natural_num = set(range(1, 10001))  # 1부터 10000까지

for i in range(10001):      # i = 850
    for j in str(i):        # j = "8", "5", "0"
        i += int(j)         # 850 + 8 + 5 + 0
    generated_num.add(i)    # 생성자가 있는 숫자들 (셀프넘버가 아님)
self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)