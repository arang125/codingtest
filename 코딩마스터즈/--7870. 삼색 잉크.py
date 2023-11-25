import sys

day_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
calendar_dict = {1:[i for i in range(1,32)], 
                 2:[i for i in range(1,29)],
                 3:[i for i in range(1,32)],
                 4:[i for i in range(1,31)],
                 5:[i for i in range(1,32)],
                 6:[i for i in range(1,31)],
                 7:[i for i in range(1,32)],
                 8:[i for i in range(1,32)],
                 9:[i for i in range(1,31)],
                 10:[i for i in range(1,32)],
                 11:[i for i in range(1,31)],
                 12:[i for i in range(1,32)]}

red = 0
blue = 0
black = 0

day = sys.stdin.readline()

day_i = day_list.index(day)

N = sys.stdin.readline()

for i in range(1,13):
    for j in range(len(calendar_dict[i])):
        calendar_dict[i][j] = day[day_i]
        day_i += 1
        if day_i == 7:
            day_i = 0

for _ in range(N):
    MONTH, DATE = sys.stdin.readline().split()
    calendar_dict[MONTH][DATE-1] = 'SUN'

for i in range(1,13):
    for j in range(len(calendar_dict[i])):
        if calendar_dict[i][j] == 'SUN':
            red += 1
        elif calendar_dict[i][j] == 'SAT':
            blue += 1
        else:
            black += 1
    
