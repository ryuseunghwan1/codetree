num = int(input())
cnt = 0
cnt_1 = 0

for _ in range(num):
    string = input()
    cnt += len(string)

    if string[0] == 'a':
        cnt_1 += 1

print(cnt, cnt_1)
