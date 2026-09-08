
b = input().split()
cnt = 0

for i in range(int(b[0])):
    c = input()

    if c == b[1]:
        cnt += 1

print(cnt)