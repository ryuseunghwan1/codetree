n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# 1. (원래 원소의 값, 원래 인덱스) 형태로 리스트를 재구성합니다.
# 문제에서 인덱스 이동 결과를 1부터 시작하는 순서로 표현하므로, 원래 인덱스도 i + 1로 저장합니다.
arr = []
for i in range(n):
    arr.append((sequence[i], i + 1))

# 2. 원소의 값을 기준으로 오름차순 정렬합니다. 
# 값이 같다면 원래 인덱스(i + 1)가 작은 순서(안정 정렬)대로 정렬됩니다.
arr.sort(key=lambda x: x[0])

# 3. 정렬 후 각각의 원소가 몇 번째(새로운 인덱스)로 이동했는지 기록할 정답 배열을 만듭니다.
# 결과 배열의 크기는 n+1로 두고, 원래 인덱스 번호 자리에 정렬 후 순서(new_idx)를 기록합니다.
answer = [0] * (n + 1)

for new_idx, (val, original_idx) in enumerate(arr):
    # enumerate는 0부터 시작하므로 순위는 new_idx + 1이 됩니다.
    answer[original_idx] = new_idx + 1

# 4. 원래 1번 원소부터 N번 원소까지 이동한 위치를 공백을 사이에 두고 출력합니다.
for i in range(1, n + 1):
    print(answer[i], end=" ")