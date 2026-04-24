arr = list(map(int, input().split()))

even = 0
odd = 0
for i in range(10):
    if i % 2 == 0:
        even += arr[i]
    else:
        odd += arr[i]

if even > odd:
    print(even - odd)
else:
    print(odd - even)