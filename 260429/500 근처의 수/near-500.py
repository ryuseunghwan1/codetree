a = list(map(int, input().split()))
mini = []
maxi = []

for i in a:
    if i < 500:
        mini.append(i)
    else:
        maxi.append(i)

print(max(mini), min(maxi))