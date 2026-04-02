classroom = 0
bokdo = 0
restroom = 0

n = int(input())

for i in range(1, n+1):
    
    if i % 12 ==0:
        restroom +=1
    elif i % 3 ==0:
        bokdo += 1
    elif i % 2 ==0:
        classroom +=1
    else:
        continue

print(classroom, bokdo, restroom)