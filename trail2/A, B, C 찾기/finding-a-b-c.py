arr = list(map(int, input().split()))

# Please write your code here.

# 오름차순으로 정렬합니다.
arr.sort()

# 정렬된 상태에서 A, B, C를 추출합니다.
A = arr[0]
B = arr[1]
C = arr[6] - A - B  # 전체 합(가장 큰 값)에서 A와 B를 빼면 C가 됩니다.

# 결과 출력
