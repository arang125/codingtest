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

# 
