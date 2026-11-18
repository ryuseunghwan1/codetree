n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

ans = 0
diff = 0  # 지금 경계선을 넘어가야 하는 사람 수
for i in range(n - 1):        # 경계선은 N-1개
    diff += A[i] - B[i]       # 누적(A) - 누적(B)
    ans += diff

print(ans