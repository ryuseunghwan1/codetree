a, b = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(b):
    cnt = list(map(int, input().split()))

    if cnt[0] == 1:
        print(arr[cnt[1]-1])
    elif cnt[0] == 2:
        print(arr.index(cnt[1])+1)
    elif cnt[0] == 3:
        for i in range(cnt[1]-1, cnt[2]):
            print(arr[i], end= ' ')
        print()
    else:
        print(0)
        
        