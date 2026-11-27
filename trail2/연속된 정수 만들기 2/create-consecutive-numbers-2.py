pos = list(map(int, input().split()))

# Please write your code here.
a, b ,c  = sorted(pos)

gap_1 = b-a
gap_2 = c-b

if (gap_1) == 1 and (gap_2) == 1:
    print(0)
elif (gap_1) == 2 or (gap_2) == 2:
    print(1)
else:
    print(2))