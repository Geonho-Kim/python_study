C = int(input())
for i in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0] # 평균 구하기
    students = 0
    for scores in nums[1:]:
        if scores > avg:
            students += 1   # 점수가 평균보다 높은 학생 수
    rate = students/nums[0] * 100
    print(f'{rate:.3f}%')   # 소수점 셋째 자리 까지
