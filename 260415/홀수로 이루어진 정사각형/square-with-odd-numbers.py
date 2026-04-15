N = int(input())

for i in range(11, 11 + (N*2), 2):
    for j in range(i, i + (N*2), 2):
        print(j, end = ' ')
    print()