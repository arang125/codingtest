# 문제 : 주어진 숫자 N개 중에서 자기 자신보다 작은 숫자가 몇 개 인지 순서대로 N번 출력

import sys

INPUT = sys.stdin.readline

N = INPUT()
nums = list(map(int, INPUT().split()))
nums_dict = {}
# answer은 처음 받은 숫자의 순서를 저장하고
answer = nums.copy()

# 중복을 제거하면서 정렬 / 중복이 있으면 나중에 인덱스를 뽑을 때 자기보다 작은 수가 자기와 같은 수를 포함하게 되니까...
nums = sorted(set(nums))

# 정렬한 수를 딕셔너리 키로 두고 정렬된 순서(인덱스)로 value값을 넣음 / 정렬된 순서만큼 자기보다 작은 수가 있는거니까!
# list.index() 얘는 O(n)이므로 for이랑 쓰면 n^2이 됨... 바꿈
for i in range(len(nums)):
    nums_dict[nums[i]] = i

# 처음에 입력받은 숫자 순서대로 딕셔너리 키를 입력해서 해당 수 보다 작은 수의 개수를 찾는다. / 정렬 + 인덱스가 해당 숫자보다 작은 수의 개수
for a in answer:
    print(nums_dict[a], end=' ')