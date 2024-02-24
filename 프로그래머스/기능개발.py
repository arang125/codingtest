def solution(progresses, speeds):
    answer = []
    tmp = []
    
    for i in range(len(progresses)):
        j = 1
        while progresses[i] + speeds[i] * j < 100:
            j += 1
        tmp.append(j)
    
    a = 1
    n = tmp[0]

    for i in range(1, len(tmp)):
        if n >= tmp[i]:
            a += 1
            
        else:
            answer.append(a)
            a = 1
            n = tmp[i]
    answer.append(a)
            
    return answer