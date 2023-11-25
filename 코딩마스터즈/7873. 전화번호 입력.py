import sys

num_list = ['0','1','2','3','4','5','6','7','8','9']
phone_num = sys.stdin.readline().rstrip()
cnt = 0

for num in phone_num:
    if num in num_list:
        cnt += 1
            
if cnt != 11 or len(phone_num) != 13:
    print('invalid')
else:
    if phone_num[:3] != '010':
        print('invalid')
    else:
        print('valid')