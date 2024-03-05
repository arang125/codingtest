def solution(answers):
    answer = []
    score = [0, 0, 0]
    answer_1 = []
    answer_2 = []
    answer_3 = []
    
    # 1
    for i in range(1, len(answers)+1):
        if i%5 > 0:
            answer_1.append(i%5)
        else:
            answer_1.append(5)
    
    # 2
    for i in range(1, len(answers)+1):
        if i%8 in [1,3,5,7]:
            answer_2.append(2)
        elif i%8 == 2:
            answer_2.append(1)
        elif i%8 == 4:
            answer_2.append(3)
        elif i%8 == 6:
            answer_2.append(4)
        else:
            answer_2.append(5)
        
    # 3
    for i in range(1, len(answers)+1):
        if i % 10 in [1,2]:
            answer_3.append(3)
        elif i % 10 in [3,4]:
            answer_3.append(1)
        elif i % 10 in [5,6]:
            answer_3.append(2)
        elif i % 10 in [7,8]:
            answer_3.append(4)
        else:
            answer_3.append(5)
            
    for i in range(len(answers)):
        if answers[i] == answer_1[i]:
            score[0] += 1
        if answers[i] == answer_2[i]:
            score[1] += 1
        if answers[i] == answer_3[i]:
            score[2] += 1
        
    if score.count(max(score)) >= 1:
        for i, num in enumerate(score):
            if num == max(score):
                answer.append(i+1)
        
    answer.sort()
    return answer