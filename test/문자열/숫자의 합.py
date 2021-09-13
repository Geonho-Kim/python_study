num = int(input())

numbers = int(input())
sum = 0
numbers_list = list(map(int, str(numbers)))
for i in numbers_list:
    sum += i
print(sum)

# a=int(input())
# b=list(input())
# result=0
#
# for i in b:
#     result += int(i)
# print(result)