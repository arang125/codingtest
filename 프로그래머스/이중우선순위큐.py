import heapq as hq
def solution(operations):
    answer = []
    min_h = [] # 걍 넣고
    max_h = [] # - 해서 넣기
    
    for operation in operations:
        i, n = operation.split()
        n = int(n)
        if i == "I":
            hq.heappush(min_h, n)
            hq.heappush(max_h, -n)
        else:
            if max_h and min_h:
                if n == 1:
                    min_h.remove(-max_h[0])
                    hq.heappop(max_h)
                else:
                    max_h.remove(-min_h[0])
                    hq.heappop(min_h)
            
        if min_h and max_h:
            answer = [-max_h[0], min_h[0]]
        elif min_h:
            answer = [min_h[0], min_h[0]]
        elif max_h:
            answer = [-max_h[0], -max_h[0]]
        else:
            answer = [0, 0]
        
    return answer