n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

min_diff = 100



for i in range(n):
    arr[i] *= 2          # 두 배로 만들고

    for j in range(n):
        remaining_arr = []
        for k in range(n):
            if j != k:
                remaining_arr.append(arr[k])

        sum_diff = 0
        for k in range(n - 2):
            sum_diff += abs(remaining_arr[k + 1] - remaining_arr[k])

        min_diff = min(min_diff, sum_diff)

    arr[i] //= 2         # ← 원래 값으로 되돌리기

print(min_diff)





