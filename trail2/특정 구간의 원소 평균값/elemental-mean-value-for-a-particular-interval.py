n = int(input())
nums = list(map(int, input().split()))

count = 0

# 모든 구간 [i, j] 를 검사 (0-indexed, i <= j)
for i in range(n):
    total = 0
    for j in range(i, n):
        total += nums[j]              # 구간 [i, j]의 합을 누적
        length = j - i + 1
        avg = total / length          # 구간 평균

        # 평균이 구간 [i, j] 안의 원소 중 하나인지 확인
        if avg in nums[i:j+1]:
            count += 1

print(count)