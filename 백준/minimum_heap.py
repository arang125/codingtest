import sys
from heapq import *

N = int(sys.stdin.readline())
h_list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(h_list) == 0:
            print(0)
        else:
            print(heappop(h_list))
    else:
        heappush(h_list, num)