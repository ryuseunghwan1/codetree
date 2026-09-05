a = input()
b = input()

cnt = 0
found = False

for i in range(len(a)):
    if a == b:
        print(cnt)
        found = True
        break
    a = a[-1] + a[:-1]  
    cnt += 1

if not found:
    print(-1)