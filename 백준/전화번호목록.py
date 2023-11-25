import sys
import collections

INPUT = sys.stdin.readline

# t는 일관성 검사 수행 횟수
t = int(INPUT())    

for _ in range(t):
    
    # 몇 개의 전화번호로 일관성 검사를 할 것인지
    n = int(INPUT())
    
    # 번호 목록 
    NUMS = []
    
    # 쪼개서.. 확인하는 목록
    C_dict = collections.defaultdict(int)
    
    answer = 1

    for _ in range(n):
        
        tmp = str(INPUT().strip())
        NUMS.append(tmp)

        # 전화번호 쪼개서 C에 넣기...
        tmp_list = ''
        
        for t in tmp:
            tmp_list += t
            C_dict[tmp_list] += 1
            print(C_dict)
    
    # 완전한 전화번호가 쪼갠 목록에 두 번 이상 있으면 일관성 X
    for NUM in NUMS:
        if C_dict[NUM] > 1:
            answer += 1
            print(NUM)
    
    if answer > 1:
        print('NO')
        print(answer)
            
    else:
        print('YES')
        print(answer)