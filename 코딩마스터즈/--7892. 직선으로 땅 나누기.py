import sys

N = int(sys.stdin.readline().strip())

if N == 1 : print(0)

else:
    x = 1
    y = 0
    
    while N > (x+1) * (y+1):
        if x == y:
            x += 1
        else:
            y += 1
            
    print(x+y)