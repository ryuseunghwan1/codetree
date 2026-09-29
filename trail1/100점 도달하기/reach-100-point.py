num = int(input())

while num <= 100:
    if num >= 90:
        print('A', end=' ')
    elif num >= 80:
        print('B', end= ' ')
    elif num >= 70:
        print('C', end=' ')
    elif num >= 60:
        print('D', end=' ')
    else:
        print('F', end=' ')
    
    num += 1