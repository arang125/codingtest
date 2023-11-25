import sys

S = str(sys.stdin.readline())

alp = 'abcdefghijklmnopqrstuvwxyz'

S = S.lower()
count = 0

for a in alp:
    if a not in S:
        count += 1
        
if count > 0:
    print('NO')
else:
    print('YES')