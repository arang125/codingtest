def solution(genres, plays):
    answer = []
    best_album = {}
    genres_dict = {}
    n = 0
    
    for i in genres:
        if i not in best_album.keys():
            best_album[i] = [[plays[n], n]]
            genres_dict[i] = plays[n]
            n += 1
        else:
            best_album[i].append([plays[n], n])
            genres_dict[i] += plays[n]
            n += 1
    
    for i in best_album.keys():
        best_album[i] = sorted_data = sorted(best_album[i], key=lambda x: (-x[0], x[1]))
    tmp = []
    
    for i in genres_dict.keys():
        tmp.append([genres_dict[i],i])

    tmp = sorted(tmp, reverse=True)
    
    for t in range(len(tmp)):
        if len(best_album[tmp[t][1]]) > 1:
            answer.append(best_album[tmp[t][1]][0][1])
            answer.append(best_album[tmp[t][1]][1][1])
        else:
            answer.append(best_album[tmp[t][1]][0][1])
               
    return answer