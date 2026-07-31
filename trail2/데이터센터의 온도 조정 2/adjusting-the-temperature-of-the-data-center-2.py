import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    N = int(data[0])
    C = int(data[1])
    G = int(data[2])
    H = int(data[3])
    
    devices = []
    temps = set() # 온도의 경계값들을 담을 집합
    
    idx = 4
    for _ in range(N):
        Ta = int(data[idx])
        Tb = int(data[idx+1])
        devices.append((Ta, Tb))
        # 작업량이 변하는 핵심 경계 온도들을 수집
        temps.add(Ta)
        temps.add(Tb)
        temps.add(Tb + 1) # Tb를 넘어가는 순간 작업량이 H로 변하므로 포함
        idx += 2

    # 아주 낮은 온도(예: 최소 Ta보다 훨씬 작은 온도)에서의 기본값도 확인해야 하므로 추가
    min_ta = min(t[0] for t in devices)
    temps.add(min_ta - 1)

    max_work = 0

    # 수집한 경계 온도들(또는 대표 온도들)을 하나씩 대입해 보며 최댓값 탐색
    for temp in temps:
        current_work = 0
        for Ta, Tb in devices:
            if temp < Ta:
                current_work += C
            elif temp <= Tb:
                current_work += G
            else:
                current_work += H
        
        max_work = max(max_work, current_work)

    print(max_work)

if __name__ == '__main__':
    solve()