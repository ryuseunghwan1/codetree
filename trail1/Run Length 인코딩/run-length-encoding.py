

# Please write your code here.
A = input()
cnt = 0
total = []
for i in range(len(A)):
    if i == 0 or A[i-1] == A[i]:
        cnt += 1
    else:
        total.append(A[i-1])
        total.append(str(cnt))
        cnt = 1

# [보완] 반복문이 끝난 후, 마지막 문자와 개수를 반드시 추가해줍니다.
if len(A) > 0:
    total.append(A[-1])
    total.append(str(cnt))

# 최종 압축된 문자열 생성
result_str = ''.join(total)

# 출력 요구사항에 맞게 압축된 '문자열의 길이'와 '문자열'을 출력합니다.
print(len(result_str))
print(result_str)