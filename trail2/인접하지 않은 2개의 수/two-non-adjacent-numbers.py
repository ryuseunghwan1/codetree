n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

cnt = 0
for i in range(n):
    for j in range(i+2, n):
        cnt = max(cnt, numbers[i] + numbers[j])

print(cnt)