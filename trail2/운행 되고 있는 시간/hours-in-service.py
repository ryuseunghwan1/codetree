n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_time = 0

# i번 개발자를 해고한다고 가정
for i in range(n):
    # 각 시간대별로 일하는 사람이 있는지 체크하기 위한 배열 (시간은 최대 1000까지)
    time_count = [0] * 1005
    
    # i번을 제외한 나머지 개발자들의 작업 시간을 체크
    for j in range(n):
        if i == j:
            continue
        
        start, end = points[j]
        # [start, end) 구간에 속하는 시간 단위에 카운트 증가
        for t in range(start, end):
            time_count[t] += 1
            
    # 직원이 1명이라도 일하고 있는 시간(합집합)의 총합 계산
    current_time = 0
    for t in range(1, 1000):
        if time_count[t] > 0:
            current_time += 1
            
    # 최댓값 갱신
    max_time = max(max_time, current_time)

print(max_time)