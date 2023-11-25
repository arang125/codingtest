import sys

X, Y, Z = map(int,sys.stdin.readline().split())

# 거리는 속력*시간...
# 시간은 거리/속력...
# 기차가 서로 부딪히는 시간은 time = X/Y+Y = X/2Y
# 파리는 기차가 부딪힐 때까지 날아다님. 즉, 거리 = (X/2Y)*Z

print((X*Z)//(Y*2))