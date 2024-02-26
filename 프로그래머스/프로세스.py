from collections import deque

def solution(priorities, location):
    answer = 0
    n = 1
    priorities_q = deque(priorities)
    seq_q = deque([x for x in range(len(priorities))])
    t = priorities[location]
    
    while answer == 0:
        if priorities_q[0] == t and priorities_q[0] == max(priorities_q) and seq_q[0] == location:
            answer = n
        elif priorities_q[0] != t and priorities_q[0] == max(priorities_q):
            priorities_q.popleft()
            seq_q.popleft()
            n += 1
        elif priorities_q[0] == t and priorities_q[0] == max(priorities_q) and seq_q[0] != location:
            priorities_q.popleft()
            seq_q.popleft()
            n += 1
        else:            
            priorities_q.append(priorities_q.popleft())
            seq_q.append(seq_q.popleft())
        
    return answer