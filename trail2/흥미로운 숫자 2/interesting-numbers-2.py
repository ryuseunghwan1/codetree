import sys

def is_interesting(num_str):
    # 자릿수가 1개인 경우는 '정확히 한 자리만 다른' 조건을 만족할 수 없음
    if len(num_str) <= 1:
        return False
        
    # 각 자릿수의 등장 횟수를 딕셔너리로 카운트
    from collections import Counter
    counts = Counter(num_str)
    
    # 자릿수가 정확히 두 종류의 숫자로만 이루어져 있어야 함 
    # (예: '33335'는 '3'이 4개, '5'가 1개 -> 총 2종류)
    if len(counts) != 2:
        return False
        
    # 두 종류 중 하나는 반드시 1번만 등장해야 함 (정확히 한 자리만 다른 숫자)
    # 다른 하나는 당연히 전체 길이 - 1 번 등장해야 함
    frequencies = list(counts.values())
    if 1 in frequencies:
        return True
        
    return False

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    X = int(data[0])
    Y = int(data[1])
    
    count = 0
    for num in range(X, Y + 1):
        if is_interesting(str(num)):
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()