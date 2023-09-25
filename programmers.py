# x만큼 간격이 있는 n개의 숫자 (lv.1)
def solution(x, n):
    answer = []
    
    if x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
    
    elif x == 0:
        for i in range(n):
            answer.append(x)
    
    else:
        for i in range(x, x*n-1, x):
            answer.append(i)
    
    return answer

# 나머지가 1이 되는 수 찾기 (lv.1)
def solution(n):
    answer = 0
    
    for i in range(2, n):
        if (n-1) % i == 0:
            answer = i
            break
            
    return answer

# 짝수와 홀수
def solution(num):
    answer = ''
    
    if num%2 == 0: answer = 'Even'
    else: answer = 'Odd'
    
    return answer

# 약수의 합
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    n = str(n)
    
    for i in range(len(n)):
        answer += int(n[i])

    return answer

# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    n = str(n)
    
    for i in range(-1,-len(n)-1,-1):
        answer.append(int(n[i]))
    
    return answer

# 문자열을 정수로 바꾸기
def solution(s):
    answer = 0
    answer = int(s)
    return answer

# 문자열 내 p와 y의 개수
def solution(s):
    answer = True
    ans_dict = {'p':0, 'y':0}
    
    for i in s:
        if (i == 'p') | (i == 'P') : ans_dict['p'] += 1
        elif (i == 'y') | (i == 'Y') : ans_dict['y'] += 1
    
    if ans_dict['p'] != ans_dict['y'] : answer = False
    
    return answer

# 