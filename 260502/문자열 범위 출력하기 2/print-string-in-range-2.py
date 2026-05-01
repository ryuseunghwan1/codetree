a= input()
num = int(input())

if len(a) > num:
    for i in range(1, num+1):
        print(a[-i], end = '')
else:
    for j in a[::-1]:
        print(j, end='')
        
