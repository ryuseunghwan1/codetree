

# 문자열 입력 받기
A = input()

# 쌍의 개수를 저장할 변수
cnt = 0

# 1. 여는 괄호 '('의 위치 i를 선택합니다.
for i in range(len(A)):
    if A[i] == '(':
        
        # 2. i보다 뒤에 있는 위치 j 중에서 닫는 괄호 ')'를 찾습니다.
        for j in range(i + 1, len(A)):
            if A[j] == ')':
                cnt += 1  # 올바른 쌍을 찾았으므로 카운트 증가

# 결과 출력
print(cnt)