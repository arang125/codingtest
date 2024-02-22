def solution(clothes):
    answer = 1
    clothes_dict = {}

    for i in clothes:
        if i[1] not in clothes_dict.keys():
            clothes_dict[i[1]] = [i[0]]
        else:
            clothes_dict[i[1]].append(i[0])

    for k in clothes_dict.keys():
        answer *= len(clothes_dict[k])+1
        
    answer -= 1
                   
    return answer