from heapq import *
import sys

N = int(sys.stdin.readline())

gifts = []

for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))

    if (nums[0] == 0) & (len(gifts) == 0):
        print(-1)
        
    elif len(nums) > 1:
        for i in range(1, len(nums)):
            gifts.append(nums[i])
        
    else:
        print(max(gifts))
        gifts.remove(max(gifts))
        
# 힙으로 하는 방법!
# import sys
# from heapq import heappush, heappop
# n = int(sys.stdin.readline())
# gifts = []
# for _ in range(n):
#     a, *values = map(int, sys.stdin.readline().split()) # unpacking 시 마지막 변수에 *을 붙이면 나머지를 리스트로 저장합니다.
#     if not a == 0:
#         for value in values:
#             heappush(gifts, -value)                     # 최대힙의 선물에 넣어줍니다.
#     else:
#         print(-heappop(gifts) if len(gifts) else -1)    # 힙에서 최댓값을 꺼내줍니다.