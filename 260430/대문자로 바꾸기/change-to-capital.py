arr = []
for _ in range(5):
    cnt_arr = list(input().split())
    arr.append(cnt_arr)

for i in arr:
    for j in i:
        print(j.upper(), end=' ')
    print()
