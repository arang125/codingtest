# import sys
# from heapq import *

# N, M = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))
# i = 1
# three_list = []
# tmp = []

# for num in nums:
#     if i <= M:
#         tmp.append(num)
#         three_list.append(num)
#         heapify(three_list)
#         print(three_list[0], end = ' ')
#         i += 1
    
#     else:
#         three_list.remove(tmp[0])
#         del tmp[0]
#         tmp.append(num)
#         heappush(three_list, num)
#         heapify(three_list)
#         print(three_list[0], end = ' ')
#         i += 1
        
# # for문 한 개인데도 안된다고...?에반데...
# import sys
# from heapq import *
# result=[]
# n, m = map(int, sys.stdin.readline().split())
# S = list(map(int, sys.stdin.readline().split()))
# cnt = 1
# for idx, num in enumerate(S):
#     if idx <= 2:
#         a=S[:idx+1]
#         heapify(a)
#         print(a[0], end=' ')
#     else:
#         a = S[cnt:cnt+m]
#         cnt += 1
#         heapify(a)
#         if idx == n-1:
#             print(a[0])
#         else:
#             print(a[0], end=' ')