a, b = map(int, input().split())
c, d = map(int, input().split())

def clean(a, b, c, d):
    cnt_1 = b - a
    cnt_2 = d - c
    
    # 겹치는 구간의 시작점과 끝점을 구합니다.
    overlap_start = max(a, c)
    overlap_end = min(b, d)
    
    # 끝점이 시작점보다 크다면 실제로 겹치는 구역이 존재하는 것입니다.
    if overlap_start < overlap_end:
        cnt_3 = overlap_end - overlap_start
    else:
        cnt_3 = 0
    
    return cnt_1 + cnt_2 - cnt_3

print(clean(a, b, c, d))