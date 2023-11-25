# import sys

# start_time = sys.stdin.readline()
# time_h = int(start_time[:2])
# time_m = int(start_time[-3:])

# N = sys.stdin.readline()
# N = int(N)
# tmp = 0

# # 총 몇 분 뒤에 울리는지
# for i in range(N):
#     tmp += i

# time_m += tmp

# # 60분이 넘으면 시간으로 변환
# while time_m >= 60:
#     time_m -= 60
#     time_h += 1

# while time_h >= 24:
#     time_h -= 24    

# if time_h < 10:
#     time_h = '0'+ str(time_h)

# if time_m < 10:
#     time_m = '0'+ str(time_m)
    
# print(str(time_h) + ":" + str(time_m))

# 시간초과

import sys

INPUT = sys.stdin.readline

start_time = INPUT().strip()
time_h, time_m = map(int, start_time.split(':'))
initial_minutes = time_h * 60 + time_m

N = int(INPUT())

total_minutes = initial_minutes + N * (N - 1) // 2

result_h, result_m = divmod(total_minutes, 60)
result_h = result_h % 24

print(f"{result_h:02d}:{result_m:02d}")
