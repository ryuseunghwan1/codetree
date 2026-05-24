# 15개의 정수를 입력받아 리스트로 저장합니다.
arr = list(map(int, input().split()))

# 오름차순으로 정렬합니다.
arr.sort()

# 정렬된 상태에서 고정된 규칙을 이용해 A, B, C를 추출합니다.
A = arr[0]
B = arr[1]
C = arr[2]

# 가장 큰 값(전체 합)에서 A, B, C를 빼서 D를 구합니다.
D = arr[14] - A - B - C
