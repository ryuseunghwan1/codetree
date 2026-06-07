n = int(input())
S = input()

# Please write your code here.

ans = 0

# 3중 for문을 이용해 모든 조합을 탐색합니다.
# i는 C의 위치, j는 O의 위치, k는 W의 위치를 의미합니다.
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 순서대로 C, O, W가 맞는지 확인합니다.
            if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
                ans += 1

# 가능한 총 가짓수 출력
