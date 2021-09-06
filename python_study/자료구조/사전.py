# key:value
# 사전 {}

cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])   # 출력 X, 종료
print(cabinet.get(5, "사용가능"))    # None 출력, 진행 // 없을경우 출력할 내용 지정 가능
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# 키 출력
print(cabinet.keys())

# value 출력
print(cabinet.values())

# 모두 출력
print(cabinet.items())

# 모두 삭제
cabinet.clear()
print(cabinet)