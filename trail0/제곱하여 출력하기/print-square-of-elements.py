a = int(input())
arr = list(map(int, input().split()))

new_arr = [x**2 for x in arr]

print(*new_arr)
