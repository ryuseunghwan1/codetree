N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
num = [0 for _ in range(N+1)]
cnt = 0

for i in student:
    num[i] += 1

for j in num:
    if j >= K:
        print(num.index(j))
        cnt += 1
        break
        

if cnt == 0:
    print(-1)
