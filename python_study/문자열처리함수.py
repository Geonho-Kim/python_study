python = 'Python is Amazing'

print(python.upper())   #대문자로 출력
print(python.lower())   #소문자로 출력
print(python[0].isupper())  #대문자인지 확인

print(len(python))  #길이 출력

print(python.replace("Python", "Java")) #문자열 변경

index = python.index("n")   #n의 위치를 찾음
print(index)
index = python.index("n", index+1)  #첫번째 index이후부터의 문자열에서 n의 위치를 찾음
print(index)

print(python.find("Java"))  #위치를 찾음(없을경우 -1)
#index = python.index("Java")    #없을경우 오류 발생
print(python.find("Amazing"))

print(python.count("n"))    #n의 갯수