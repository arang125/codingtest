def solution(nums):
    answer = 0
    ponketmon = {}
    for i in nums:
        if i in ponketmon:
            ponketmon[i] += 1
        else:
            ponketmon[i] = 0
    if len(nums) / 2 >= len(ponketmon):
        answer = len(ponketmon)
    else:
        answer = len(nums)/2
    return answer