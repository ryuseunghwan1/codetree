arr = map(int, input().split())
arr_1 = list(arr)


def get_diff(i, j, m):
    sum1 = arr_1[i] + arr_1[j] + arr_1[m]
    sum2 = sum(arr_1) - sum1
    return abs(sum1 - sum2)

min_diff = 1000000

for i in range(0, 6):
    for j in range(i+1, 6):
        for m in range(j+1, 6):
            min_diff = min(min_diff, get_diff(i, j, m))

print(min_diff)