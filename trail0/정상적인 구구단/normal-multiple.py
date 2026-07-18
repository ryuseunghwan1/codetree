num = int(input())

for i in range(1, num+1):
    row = []
    for j in range(1, num+1):
        row.append(f"{i} * {j} = {i*j}")
    
    print(", ".join(row))