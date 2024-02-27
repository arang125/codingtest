from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        now = q.popleft()
        answer.append(0)
        for price in q:
            answer[-1] += 1
            if price < now:
                break
    
    return answer