num = int(input())
string = []

for i in range(num):
    a = input()
    string.append(a)

ques = input()
cnt = 0
cnt_1 = 0

for j in string:
    if j[0] == ques:
        cnt += 1
        cnt_1 += len(j)

print(cnt, format(cnt_1/cnt, ".2f"))