import sys

N, M = map(int, sys.stdin.readline().split())

# N줄에 걸쳐 각 줄에 M개의 문자

# 오른쪽으로 k칸 + 아래쪽으로 k칸 = 구역 축복(?)
# 최대 축복보다 구역 축복이 크면 업데이트

# 땅 만들기
land = [[0]*M for i in range(N)]
for i in range(N):
    tmp = str(sys.stdin.readline())
    for j in range(M):
        land[i][j] = tmp[j]

# 탐색 범위는 land[0][0]~land[N][M]
def pungsu(i, j):
    visit[i][j] = 1
    bless = 1
    if 
    
    

# 한 번 탐색한 땅은 다시 탐색하지 않기 위해 0 -> 1로 업데이트
visit = [[0]*M for i in range(N)]

# 탐색한 땅 표시
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            pungsu(i, j)