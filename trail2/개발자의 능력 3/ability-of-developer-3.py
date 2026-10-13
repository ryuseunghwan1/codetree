import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = 6
arr = list(map(int, input().split()))


def diff(i, j, k):
    # 두 번째 팀원의 합은 전체에서 첫 번째 팀원의 합을 빼주면 됩니다.
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)


# 첫 번째 팀원을 만들어줍니다.
min_diff = INT_MAX
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            min_diff = min(min_diff, diff(i, j, k))
    
print(min_diff)
