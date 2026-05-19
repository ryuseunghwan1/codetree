
# N1, N2 입력 받기
n1, n2 = map(int, input().split())

# 수열 A와 수열 B 입력 받기
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# 수열 B가 수열 A의 연속부분수열인지 확인할 변수
is_subsequence = False

# 수열 A에서 수열 B가 시작할 수 있는 모든 위치(i)를 탐색합니다.
for i in range(n1 - n2 + 1):
    
    # 현재 위치 i부터 n2개의 원소가 수열 B와 완전히 일치하는지 확인합니다.
    match = True
    for j in range(n2):
        if arr_a[i + j] != arr_b[j]:
            match = False
            break  # 하나라도 다르면 현재 시작점(i)은 실패이므로 탈출
            
    # 완벽하게 일치하는 구간을 찾았다면 변수를 True로 바꾸고 탐색 종료
    if match:
        is_subsequence = True
        break

# 결과 출력
if is_subsequence:
    print("Yes")
else:
    print("No")