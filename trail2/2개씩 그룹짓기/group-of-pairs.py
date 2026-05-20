n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

# 1. 2N개의 숫자를 오름차순으로 정렬합니다.
nums.sort()

max_sum = 0

# 2. 가장 작은 값(i)과 가장 큰 값(2n - 1 - i)을 쌍으로 묶어 합을 구합니다.
# 그룹의 총 개수는 N개이므로 N번 반복합니다.
for i in range(n):
    # 양 끝값의 합 계산
    current_sum = nums[i] + nums[2 * n - 1 - i]
    
    # 그 중 최댓값을 계속 갱신합니다.
    if current_sum > max_sum:
        max_sum = current_sum

# 3. 계산된 최댓값 중 가장 최소가 되는 (정렬 매칭의) 결과를 출력합니다.
print(max_sum)