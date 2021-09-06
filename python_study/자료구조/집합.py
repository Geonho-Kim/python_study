# 집합 set
# 중복 X, 순서 X

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "조세호", "김태호"}
python = set(["유재석", "박명수"])

# 교집합 (java, python 모두 가능한 사람
print(java & python)
print(java.intersection(python))

# 합집합 (java, python 둘중 하나라도 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 수 없는 사람)
print(java - python)
print(java.difference(python))

# python을 할 수 있는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊음
java.remove("김태호")
print(java)