s = input()
list_a = list(range(97, 123))   # 아스키코드 a부터 z까지 리스트
for i in list_a:
    print(s.find(chr(i)))   # 입력 받은 문자열에서 알파벳의 위치를 찾음. 없을경우 -1을 출력
