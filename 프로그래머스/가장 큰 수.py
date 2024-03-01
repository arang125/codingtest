def solution(numbers):
    answer = ''
    tmp_list = []
    
    while numbers:
        tmp_list.append(str(numbers.pop()))
        
    tmp_list = sorted(tmp_list, key = lambda x: x*4)
    
    while tmp_list:
        answer += tmp_list.pop()
    
    while True:
        if len(answer) > 1 and answer[0] == '0':
            answer = answer[1:]
        else:
            break
    
    return answer