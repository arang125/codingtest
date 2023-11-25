N = int(input())
gift = []

for i in range(N):
    tmp = int(input().split())
    if tmp != 0:
        gift.append(tmp)
    
    else:
        if len(gift)>0:
            print(max(gift))
            gift.remove(max(gift))
        else:
            print(-1)
        