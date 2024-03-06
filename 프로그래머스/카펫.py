def solution(brown, yellow):
    answer = [3, 3]
    S = brown + yellow
    a = 2
    tmp = []
    
    while S > a:
        a += 1
        if S%a == 0 and a >= 3 and S/a >= 3 and a >= S/a:
            tmp.append([a, S/a])
    
    if len(tmp) == 1:
        answer = tmp[0]
    else:
        for i in tmp:
            if (i[0]-2)*(i[1]-2) == yellow:
                answer = [i[0],i[1]]
                
    return answer