import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    N = int(data[0])
    a = [int(x) for x in data[1:N+1]]
    
    # 각 K가 만들 수 있는 등차수열의 개수를 저장할 딕셔너리
    k_count = defaultdict(int)
    
    # 모든 (a_i, a_j) 조합 확인 (i < j)
    for i in range(N):
        for j in range(i + 1, N):
            s = a[i] + a[j]
            # 두 수의 합이 짝수여야 K가 정수가 됨
            if s % 2 == 0:
                K = s // 2
                k_count[K] += 1
                
    # 만약 만들 수 있는 등차수열이 하나도 없다면 0 출력
    if not k_count:
        print(0)
    else:
        # 가장 많이 만들어지는 등차수열의 개수(최댓값) 출력
        print(max(k_count.values()))

if __name__ == '__main__':
    solve()