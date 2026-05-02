count_ee = 0
count_eb = 0

a = input()

for i in range(len(a)-1):
    if a[i] + a[i+1] == 'ee':
        count_ee += 1

for j in range(len(a)-1):
    if a[j] + a[j+1] == 'eb':
        count_eb += 1

print(count_ee, count_eb)