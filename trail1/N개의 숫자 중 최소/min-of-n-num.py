# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# 초기값을 적습니다. 최소가 될 첫 번째 후보입니다.
min_val = arr[0]
cnt = 1 # Case 1

# 나머지 원소들을 보며 답을 갱신합니다.
for i in range(1, n):
    # Case 1
    if min_val > arr[i]:  # 지금까지 나왔던 값들 보다 더 작은 값이라면
        min_val = arr[i]  # 최초의 최솟값이 되므로 그 값을 갱신하고
        cnt = 1           # Count를 1로 초기화합니다.
    # Case 2
    elif min_val == arr[i]:   # 지금까지의 최소와 같다면
        cnt += 1          # Count를 1 증가시켜줍니다.

# 출력
print(min_val, cnt)
