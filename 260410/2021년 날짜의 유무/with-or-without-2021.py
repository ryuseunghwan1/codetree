M, D = map(int, input().split())


# Please write your code here.

def calender(a,b):
    M = False
    D = False

    if a <= 12:
        M = True

    if a in [1, 3, 5, 7, 8, 10, 12] and b <= 31:
        D = True
    elif a == 2 and b <= 28:
        D = True
    elif a in [4, 6, 9, 11] and b <= 30:
        D = True
    
    return M & D

if calender(M,D) == True:
    print('Yes')
else:
    print('No')

