m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
calender = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a, b = d1, d2

for i in range(m1-1, 0, -1):
    a += calender[i] 

for j in range(m2-1, 0, -1):
    b += calender[j]

print(b-a+1)