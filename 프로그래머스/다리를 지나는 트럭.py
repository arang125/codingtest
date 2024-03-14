from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    cross_bridge = [0] * bridge_length
    cross_sum = 0
    
    while truck_weights:
        if cross_sum - cross_bridge[0] + truck_weights[0] <= weight:
            cross_sum += truck_weights[0] - cross_bridge[0]
            cross_bridge.pop(0)
            cross_bridge.append(truck_weights.popleft())
            answer += 1
        else:
            if cross_bridge[0] == 0:
                cross_bridge.append(cross_bridge.pop(0))
                answer += 1
            else:
                cross_sum -= cross_bridge.pop(0)
                cross_bridge.append(0)
                answer += 1
    
    answer += bridge_length
    
    return answer