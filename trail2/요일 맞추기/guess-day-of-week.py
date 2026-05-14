m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

wkd = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

total_1 = d1
total_2 = d2

for i in range(m1-1, 0, -1):
    total_1 += month[i]

for j in range(m2-1, 0 , -1):
    total_2 += month[j]

if total_1 - total_2 < -7:
    print(wkd[(total_1 - total_2) % 7])
elif total_1 - total_2 > 6:
    print(wkd[(total_1 - total_2) % 7])
else:
    print(wkd[-(total_1 - total_2)])