import sys

A, B, C = map(int, sys.stdin.readline().split())

i = 1

while A * i < C * 10:
    i += 1

print(i)