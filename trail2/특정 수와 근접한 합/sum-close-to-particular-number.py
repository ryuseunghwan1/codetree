a, b = map(int, input().split())
arr_1 = list(map(int, input().split()))

total_sum = sum(arr_1)
min_diff = float('inf')

for i in range(a):
    for j in range(i + 1, a):
        remaining_sum = total_sum - (arr_1[i] + arr_1[j])

        diff = abs(remaining_sum - b)

        min_diff = min(min_diff, diff)

print(min_diff)