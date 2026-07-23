string = []
for _ in range(10):
    a = input()
    string.append(a)

ques = input()
cnt = 0

for i in string:
    if i[-1] == ques:
        print(i)
        cnt += 1

if cnt == 0:
    print('None')
