def solution(participant, completion):
    answer = ''
    completion.append(' ')
    
    participant=sorted(participant, reverse=True)
    completion=sorted(completion, reverse=True)
    
    for i in range(len(participant)):
        if participant[i] == completion[i]:
            continue
        else:
            answer = participant[i]
            break
    
    return answer