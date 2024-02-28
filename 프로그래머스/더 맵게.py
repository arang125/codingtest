import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if min(scoville) < K:
        while scoville[0] < K:
            if len(scoville) < 2:
                answer = -1
                break
            else:
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)*2    
                heapq.heappush(scoville, a+b)
                answer += 1
        
    return answer