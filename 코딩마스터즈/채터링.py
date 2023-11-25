# -*- coding: utf-8 -*-
# import sys

# N, K = map(int, sys.stdin.readline().split())

# chat = str(sys.stdin.readline())

# for c in chat:
#     print(c*K, end="")
    
    # -*- coding: utf-8 -*-
import sys

N, K = map(int, sys.stdin.readline().split())

chat = str(sys.stdin.readline())

for i in range(N):
    print(chat[i]*K, end="")
    
    # 둘이 다른 점이 뭘까...?