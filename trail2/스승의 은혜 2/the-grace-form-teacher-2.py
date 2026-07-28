n, b = map(int, input().split())
p = [int(input()) for _ in range(n)]

max_students = 0

for i in range(n):
    points_p = p.copy()
    points_p[i] = points_p[i] // 2

    points_p.sort()

    cnt = 0
    total_cost = 0

    for price in points_p:
        if total_cost + price <= b:
            total_cost += price
            cnt += 1
        
        else:
            break

    max_students = max(max_students, cnt)

print(max_students)