a = input()
b = input()
count = 0
for i in range(len(a)):
    if b == a[i-1] + a[i]:
        count += 1

print(count)