import sys

INPUT = sys.stdin.readline

# N번 입력 받음
N = int(INPUT())

# 개미굴 전체 음식 리스트
all_foods = []

for _ in range(N):
    
    # K = 먹이 정보 개수, *food = 음식 리스트
    K, *food_list = str(INPUT()).split()
    
    # 전체 먹이 리스트에 먹이 리스트를 통째로 넣기
    all_foods.append(food_list)

# 한번 출력한 먹이굴 정보들 저장
answer = []

for i in range(len(all_foods)):
    
    # 전체 먹이 리스트 중에 가장 작은 값 출력
    tmp = min(all_foods)
    
    # 출력한 먹이굴 정보, 제일 위의 먹이굴마다 리셋
    tmp2_list = ''
    
    for idx, t in enumerate(tmp):
        
        # tmp2는 출력할 내용
        tmp2 = '--'*idx + t
        
        # 먹이굴 정보
        tmp2_list += tmp2
        
        # 이전에 출력한 먹이굴 정보들에 이번 먹이굴 정보가 없으면 출력하고 이번거 저장
        if tmp2_list not in answer:
            answer.append(tmp2_list)
            print('--'*idx + t)
    
    # 한번 출력한 먹이굴 정보는 삭제
    all_foods.remove(tmp)