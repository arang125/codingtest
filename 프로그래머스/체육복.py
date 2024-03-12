def solution(n, lost, reserve):
    answer = 0
    lendable_list = list(set(reserve) - set(lost))
    lost = list(set(lost) - set(reserve))
    lendable_list.sort()
    lost.sort()
    
    for i in range(1, n+1):
        if i in lost:
            for lend in lendable_list:
                if lend == i-1 or lend == i+1:
                    lost.remove(i)
                    lendable_list.remove(lend)
                    answer += 1
                    break
        else:
            answer += 1
    
    return answer