import sys

nums = []

tmp = sys.stdin.readline()

for t in range(len(tmp)):
    nums.append(tmp[t])

nums.sort()

nums2 = []

tmp = sys.stdin.readline()

for t in range(len(tmp)):
    nums2.append(tmp[t])

nums2.sort()

if nums == nums2:
    print('YES')
else:
    print('NO')