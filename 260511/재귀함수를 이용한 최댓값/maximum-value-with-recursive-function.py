n = int(input())
arr = list(map(int, input().split()))

# index번째 원소부터 마지막 원소까지 중 최댓값을 반환하는 함수
def get_max(index):
    # Base Case: 마지막 원소에 도달했을 경우 해당 원소 반환
    if index == n - 1:
        return arr[index]
    
    # Recursive Step: 
    # 현재 원소와 (현재 원소 이후의 원소들 중 최댓값)을 비교하여 더 큰 값 반환
    return max(arr[index], get_max(index + 1))

# 0번째 인덱스부터 탐색 시작
print(get_max(0))