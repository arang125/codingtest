# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

import sys
# 동갑일때 이름을 리스트로 딕셔너리 value에 저장하기 위해서 import함
from collections import defaultdict

INPUT = sys.stdin.readline

N = int(INPUT())
# name을 리스트로 저장하려고 만들었다.
member_dict = defaultdict(list)
# key는 나이로 순서를 매기려고 따로 저장함
keys = []

# 나이를 key로, 이름을 리스트로 value 값으로 딕셔너리로 저장
for i in range(N):
    age, name = INPUT().split()
    member_dict[int(age)].append(name)
    keys.append(int(age))

# 나이순으로 정렬 / 동갑인 경우 두번 출력될 가능성이 있으니까 중복 제거해서 정렬
keys = sorted(set(keys))

# keys는 나이순으로 정렬을 했으므로 나이가 어린 순서대로 딕셔너리에서 꺼내서 출력한다.
# 동갑일 경우 이름은 먼저 입력된 순서로 저장이 됐기 때문에 먼저 들어온거 먼저 출력해줌
for key in keys:
    # value 값이 1개인 경우는 동갑이 없으니까 이름 리스트의 0번 출력
    if len(member_dict[key]) == 1:
        print(f'{key} {member_dict[key][0]}')
    # value 값이 1개 초과인 경우는 동갑이 있는 경우니까 리스트에 먼저 들어온 순서로 출력
    else:
        for i in range(len(member_dict[key])):
            print(f'{key} {member_dict[key][i]}')