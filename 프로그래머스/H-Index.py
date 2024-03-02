def solution(citations):
    answer = 0
    citations_num = []
    
    for i in range(len(citations)):
        citations_num.append([0, citations[i]])
        for j in citations:
            if citations[i] <= j:
                if citations[i] != 0:
                    citations_num[i][0] += 1
    
    citations_num.sort()
    
    h_index = []
    for i in citations_num:
        if i[1] >= i[0]:
            h_index.append(i)
    
    return max(h_index)[0]