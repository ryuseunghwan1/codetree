n = int(input())

# (점의 번호, 맨해튼 거리)를 튜플로 묶어서 리스트에 저장합니다.
# 문제에서 점의 번호는 1번부터 시작하므로 i + 1을 해줍니다.
distances = []
for i in range(n):
    x, y = map(int, input().split())
    # 원점(0,0)과의 맨해튼 거리는 |x| + |y| 입니다.
    dist = abs(x) + abs(y)
    distances.append((i + 1, dist))

# 정렬 기준(key) 설정: 
# 1순위: 거리(x[1]) 오름차순
# 2순위: 거리가 같다면 번호(x[0]) 오름차순
distances.sort(key=lambda x: (x[1], x[0]))

# 정렬된 순서대로 점의 번호만 출력합니다.
for num, dist in distances:
    print(num)