num = int(input())
cnt = True
for i in range(2, num):
    if num % i == 0:
        cnt = False
        break

if cnt:
    print('P')
else:
    print('C')

        

    
