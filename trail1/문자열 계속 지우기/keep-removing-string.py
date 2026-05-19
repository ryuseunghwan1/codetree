A = input()
B = input()

# Please write your code here.

while B in A:
    # A에서 처음으로 등장하는 B를 찾아 한 번만('') 제거합니다.
    # replace(B, '', 1)에서 숫자 1은 가장 처음 매칭되는 1개만 바꾼다는 뜻입니다.
    A = A.replace(B, '', 1)

# 더 이상 B가 없을 때 남은 A를 출력합니다.
print(A)