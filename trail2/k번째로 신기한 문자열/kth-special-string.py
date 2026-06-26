n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
cnt = []
for i in str:
    if t == i[:len(t)]:
        cnt.append(i)

cnt.sort()
print(cnt[k-1])