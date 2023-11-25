import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# str2를 두 번 이어붙임
tmp = str2 + str2
answer = 0

# str1의 길이만큼만 반복
for i in range(len(str1)):
    # tmp[i:i+len(str1)]이 str1과 일치하는지 검사
    if tmp[i:i+len(str1)] == str1:
        answer += 1

# 회전된 형태가 존재하는지 여부 출력
if answer > 0:
    print('YES')
else:
    print('NO')
