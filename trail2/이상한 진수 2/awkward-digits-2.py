a = input()
max_n = 0

for i in range(len(a)):

    temp = list(a)
    if temp[i] == '0':
        temp[i] = '1'
    else:
        temp[i] = '0'

    binary_str = "".join(temp)
    current_n = int(binary_str, 2)

    max_n = max(max_n, current_n)

print(max_n)