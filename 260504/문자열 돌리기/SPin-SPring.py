a = input()
for i in range(len(a)+1):
    print(a[-i:] + a[:-i])