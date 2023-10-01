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
#==================================================================#
# 나머지가 1이 되는 수 찾기 (lv.1)
def solution(n):
    answer = 0
    
    for i in range(2, n):
        if (n-1) % i == 0:
            answer = i
            break
            
    return answer
#==================================================================#
# 짝수와 홀수
def solution(num):
    answer = ''
    
    if num%2 == 0: answer = 'Even'
    else: answer = 'Odd'
    
    return answer
#==================================================================#
# 약수의 합
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    
    return answer
#==================================================================#
# 자릿수 더하기
def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    n = str(n)
    
    for i in range(len(n)):
        answer += int(n[i])

    return answer
#==================================================================#
# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    n = str(n)
    
    for i in range(-1,-len(n)-1,-1):
        answer.append(int(n[i]))
    
    return answer
#==================================================================#
# 문자열을 정수로 바꾸기
def solution(s):
    answer = 0
    answer = int(s)
    return answer
#==================================================================#
# 문자열 내 p와 y의 개수
def solution(s):
    answer = True
    ans_dict = {'p':0, 'y':0}
    
    for i in s:
        if (i == 'p') | (i == 'P') : ans_dict['p'] += 1
        elif (i == 'y') | (i == 'Y') : ans_dict['y'] += 1
    
    if ans_dict['p'] != ans_dict['y'] : answer = False
    
    return answer
#==================================================================#
# 정수 제곱근 판별
import math

def solution(n):
    answer = 0
    # n을 제곱근으로 나눠서 나머지가 0 이면 제곱이고 나머지가 있으면 제곱이 아님
    if (n % math.sqrt(n)) == 0:
        answer = (math.sqrt(n) + 1) ** 2
    else:
        answer = -1
    return answer
#==================================================================#
# 정수 내림차순으로 배치하기
def solution(n):
    answer = ''
    list_n = []
    
    # 문자로 바꿔서 리스트에 하나씩 저장
    n = str(n)
    for i in n:
        list_n.append(i)
    # 리스트에 문자를 다시 int로 변환    
    for i in list_n:
        i = int(i)
    # 큰 숫자부터 정렬
    list_n.sort(reverse=True)
    # 문자로 변환해서 answer에 붙이기
    for i in list_n:
        answer += str(i)
    return int(answer)
#==================================================================#
# 하샤드 수
def solution(x):
    answer = True
    harshad = 0
    n = x
    
    # n을 일의 자리~n의 자리 수를 더해서 하샤드 수인지 판별하기
    while n > 0 :
        harshad += n % 10
        n = (n - (n % 10)) / 10
    
    # x를 판별하려는 수로 나눴을 때 나머지가 0이 아니면 하샤드 수가 아니므로 answer = False
    if x % harshad != 0 :
        answer = False
    
    return answer
#==================================================================#