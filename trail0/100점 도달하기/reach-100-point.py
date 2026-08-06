n = int(input())

for i in range(100-n + 1):
    if n + i >= 90:
        print("A", end=" ")
    elif n+i >= 80:
        print("B", end= " ")
    elif n+i >= 70:
        print('C', end= " ")
    elif n+i >= 60:
        print('D', end=" ")
    else:
        print("F", end = " ")