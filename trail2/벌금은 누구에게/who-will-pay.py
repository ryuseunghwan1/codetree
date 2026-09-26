N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]




arr = [0] * (N+1)
fined_student = -1
for i in student:
    arr[i] += 1

    if arr[i] >= K:
        fined_student = i
        break

print(fined_student)