# -*- coding: utf-8 -*-
import sys

N, M= map(int, sys.stdin.readline().split())

nums = list(map(str, sys.stdin.readline().split()))

# 기본은 10진법

len_n = 0

for num in nums:
    len_n += len(num) + 1
    
len_n -= -1

jin = 10

def jin_trans(num, jin):
    num = int(num)
    digits = []
    while num > 0:
        digits.append(chr(num % jin + ord('a') - 1))
        num //= jin
    return ''.join(digits[::-1])

if len_n <= M:
    print(jin)
    
else:
    for i in range(11, 65):
        trans_nums = ''
        for num in nums:
            tmp = jin_trans(num, i)
            trans_nums += tmp + ' '
            
        if len(trans_nums)-1 <= M:
            print(i)
            break
            
        elif i > 61:
            print(-1)
            break