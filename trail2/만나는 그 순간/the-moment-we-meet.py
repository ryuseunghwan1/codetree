n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.

pos_A = [0]
current_1 = 0

for direction, time in zip(d, t):
    for _ in range(time):
        if direction == 'R':
            current_1 += 1
        else:
            current_1 -= 1
        pos_A.append(current_1)

pos_B = [0]
current_2 = 0

for direction_2, time_2 in zip(d2, t2):
    for _ in range(time_2):
        if direction_2 == 'R':
            current_2 += 1
        else:
            current_2 -= 1
        pos_B.append(current_2)

ans = -1
for i in range(1, len(pos_A)):
    if pos_A[i] == pos_B[i]:
        ans = i
        break
    
print(ans)