Y, M, D = map(int, input().split())

# Please write your code here.

def calendar(Y):
    return (Y % 400 == 0) or (Y % 4 == 0 and Y % 100 != 0)

def calender_2(Y, M, D):
    
    a = 'Spring'
    b = 'Summer'
    c = 'Fall'
    d = 'Winter'

    if calendar(Y) == True:
        if M in [3, 5] and D <=31:
            return a
        elif M == 4 and D <= 30:
            return a
        elif M == 6 and D <= 30:
            return b
        elif M in [7,8] and D <= 31:
            return b
        elif M in [9, 11] and D <= 30:
            return c
        elif M == 10 and D <= 31:
            return c
        elif M in [12, 1] and D <= 31:
            return d
        elif M == 2 and D <= 29:
            return d
        else:
            return -1
    else:
        if M in [3, 5] and D <=31:
            return a
        elif M == 4 and D <= 30:
            return a
        elif M == 6 and D <= 30:
            return b
        elif M in [7,8] and D <= 31:
            return b
        elif M in [9, 11] and D <= 30:
            return c
        elif M == 10 and D <= 31:
            return c
        elif M in [12, 1] and D <= 31:
            return d
        elif M == 2 and D <= 28:
            return d
        else:
            return -1

print(calender_2(Y, M, D))