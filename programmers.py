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
# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a<b:
        for i in range(a,b+1):
            answer += i
    else :
        for i in range(b, a+1):
            answer += i
    return answer
#==================================================================#
# 콜라츠 추측
def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    
    else:
        while num != 1:
            if num % 2 == 0:
                num /= 2
                answer += 1
            else:
                num = (num * 3) + 1
                answer += 1
                
    if answer >= 500 :
        answer = -1
        
    return answer
#==================================================================#
# 서울에서 김서방 찾기
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = f"김서방은 {i}에 있다"
    return answer
#==================================================================#
# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer
#==================================================================#
# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0: 
        answer.append(-1)
    else:
        list.sort(answer)
    return answer
#==================================================================#
# 핸드폰 번호 가리기
def solution(phone_number):
    answer = ''
    answer += '*'*(len(phone_number)-4)
    for i in range(-4,0):
        answer += phone_number[i]
    return answer
#==================================================================#
# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    num = list(range(10))
    
    for i in num:
        if i not in numbers:
            answer += i
            
    return answer
#==================================================================#
# 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
    return arr
#==================================================================#
# 가운데 글자 가져오기
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        mid = len(s)//2
        answer += s[mid-1]
        answer += s[mid]
    else:
        mid = len(s)//2
        answer += s[mid]
    return answer
#==================================================================#
# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer
#==================================================================#
# 내적
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
#==================================================================#
# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        tmp = 0
        for j in range(1, i+1):
            if i % j == 0:
                tmp += 1
        if tmp % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
#==================================================================#
# 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    total_price = 0
    i = 1
    
    while i <= count :
        total_price += price * i
        i += 1
    
    if total_price > money:
        answer = total_price - money
    else:
        answer = 0
        
    return answer
#==================================================================#
# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''
    
    tmp = sorted(s, reverse=True)
    
    for i in tmp:
        answer += i
    
    return answer
#==================================================================#
# 문자열 다루기 기본
def solution(s):
    answer = False
    
    if ((len(s) == 4) | (len(s) == 6)) & (s.isdigit()):
        answer = True
            
    return answer
#==================================================================#
# 행렬의 덧셈
def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for i in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer
#==================================================================#
