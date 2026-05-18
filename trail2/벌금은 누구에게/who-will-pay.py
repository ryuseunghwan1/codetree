N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
num = [0 for _ in range(N+1)]

for i in student:
    num[i] += 1

for j in num:
    if j >= K:
        print(num.index(j))
    else:
        print(-1)