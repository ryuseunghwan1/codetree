a, b, c = map(int, input().split())

# Please write your code here.
d, e, f = 11*(24*60), 11*60, 11
a, b, c = a*(24*60), (b*60), c

total_1 = a + b + c
total_2 = d + e + f

if total_1 > total_2:
    print(total_1 - total_2)
elif total_1 == total_2:
    print(0)
else:
    print(-1)