summ = 0
aver = 0


for i  in range(10):
    num = int(input())
    
    if 0 <= num <= 200:
        summ += num
        aver += 1

print(summ, round(summ / aver, 1)