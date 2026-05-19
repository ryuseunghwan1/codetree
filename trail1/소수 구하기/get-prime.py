n = int(input())

# 1부터 n까지의 모든 수를 확인합니다.
for i in range(1, n + 1):
    # 1은 소수가 아니므로 제외합니다.
    if i == 1:
        continue
    
    is_prime = True  # i가 소수인지 판별하기 위한 기준 변수
    
    # 2부터 i-1까지의 수로 i를 나누어봅니다.
    for j in range(2, i):
        if i % j == 0:
            is_prime = False  # 하나라도 나누어떨어지면 소수가 아님
            break             # 더 이상 확인할 필요 없으므로 탈출
            
    # 위 반복문을 다 돌았는데도 나누어떨어지는 수가 없었다면 소수입니다.
    if is_prime:
        print(i, end=" ")