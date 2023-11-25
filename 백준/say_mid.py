from heapq import *
import sys

N = int(sys.stdin.readline())

small_h = []
big_h = []

for i in range(N):
    tmp = int(sys.stdin.readline())
    
    if len(small_h) == len(big_h):
        heappush(small_h, -tmp)
        
    else:
        heappush(big_h, tmp)
        
    if (len(small_h) > 0) and (len(big_h) > 0):
        if -small_h[0] > big_h[0]:
            heappush(big_h,-heappop(small_h))
            heappush(small_h,-heappop(big_h))
        
    print(-small_h[0])
    
# from heapq import *
# import sys

# INPUT = sys.stdin.readline()

# N = int(INPUT)

# def sorted_heap(nums):
#     tmp_list = list()
#     sorted_list = list()
#     for num in nums:
#         heappush(tmp_list,num)

#     while tmp_list:
#         sorted_list.append(heappop(tmp_list))
    
#     return sorted_list

# nums = list()

# for i in range(N):
#     # 입력받은 숫자를 h_list에 추가
#     nums.append(int(INPUT))
    
#     sorted_nums = sorted_heap(nums)
    
#     if len(sorted_nums) % 2 != 0:
#         print(sorted_nums[len(sorted_nums)//2])
#     else:
#         print(sorted_nums[len(sorted_nums)//2-1])
    
# 1. 한자리 숫자를 입력 받을 횟수 N을 입력 받는다.
# 2. 숫자를 한자리씩 입력 받아서 중간 숫자 출력(정렬이 되어야 한다는 뜻), 짝수 길이면 더 작은 쪽을 출력 -> heappush로 숫자를 넣으면 heappop으로 최솟값을 출력함.
# 3. 리스트를 받아서 힙으로 정렬해서 리턴(리스트가 정렬되어 나옴)
# 4. 그러면 리스트의 길이//2
# 근데 왜 sorted로 정렬하면 안되는걸까...

# 위의 방식은 시간초과...