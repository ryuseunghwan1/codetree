N = int(input())

cnt = 1

# 2차원 array 만들기
A = [[0]*N for _ in range(N)]

# 상하 반복문 작성해서 A array에 차례대로 삽입
for i in range(N):
    if i % 2 ==0:
        for j in range(N):
            A[j][i] = cnt
            cnt += 1
    else:
        for m in range(N):
            A[m][i] = cnt - 1
            cnt -= 1
            

# 다시 A array를 차례대로 print
for i in range(N):
    for j in range(N):
        print(A[i][j], end='')
    print()