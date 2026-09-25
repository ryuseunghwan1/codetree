import sys 
n = int(input())
A = list(map(int, input().split()))

min_total_distance = sys.maxsize

for i in range(n):
    current_distance_sum = 0

    for j in range(n):
        current_distance_sum += abs(i-j) * A[j]

    min_total_distacne = min(min_total_distance, current_distance_sum)

print(min_total_distance)
