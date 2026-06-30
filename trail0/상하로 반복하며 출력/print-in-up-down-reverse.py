n = int(int)     # 정사각형의 크기   # 수의 시작 값
arr = [[0 for i in range(n)] for i in range(n)] # 1단계: 2차원 배열 만들기

for i in range(n):
    cnt = 1
    if i % 2 != 0:
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt +=1 
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1
            
# 4단계: 출력하기
for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
