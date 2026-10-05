cmds = input().strip()



print(answer)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d= 0
time = 0
answer = -1

for cmd in cmds:
    time += 1

    if cmd == 'R':
        d = (d + 1) % 4
    elif cmd == 'L':
        d = (d-1)%4
    else:
        x += dx[d]
        y += dy[d]

    if x ==0 and y ==0:
        answeer = time
        break

print(answer)