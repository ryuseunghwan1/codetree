N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

result = list(zip(pigeon, position))

from collections import Counter

# 1. 첫 번째 원소들만 뽑아서 빈도수 계산
first_elements = [item[0] for item in result]
counter = Counter(first_elements)

# 2. 첫 번째 원소의 등장 횟수가 2 이상인 튜플들만 남기기
filtered_data = [item for item in result if counter[item[0]] >= 2]

# --- 이어서 작성할 코드 ---

# 각 비둘기 번호별로 등장하는 위치 기록하기
pigeon_history = {}
for p_num, pos in filtered_data:
    if p_num not in pigeon_history:
        pigeon_history[p_num] = []
    pigeon_history[p_num].append(pos)

total_crossings = 0

# 비둘기별로 위치가 바뀐 횟수 계산
for p_num, hist in pigeon_history.items():
    for i in range(len(hist) - 1):
        # 이전 위치와 현재 위치가 다르면 도로를 건넌 것임
        if hist[i] != hist[i + 1]:
            total_crossings += 1

print(total_crossings)