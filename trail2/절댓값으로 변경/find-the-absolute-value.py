

n = int(input())
arr = list(map(int, input().split()))

def make_abs(arr):
    for i in range(n):
        arr[i] = abs(arr[i])

    return

make_abs(arr)

for elem in arr:
    print(elem, end= ' ')
print()