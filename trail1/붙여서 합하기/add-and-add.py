# 문자열을 구현하여 입력받습니다.
a, b = tuple(input().split())

# str1에는 a, b 순으로 문자열을 붙입니다.
str1 = a + b

# str2에는 b, a 순으로 문자열을 붙입니다.
str2 = b + a

# 합쳐진 문자열을 숫자로 바꿉니다.
str1_int = int(str1)
str2_int = int(str2)
    
# 두 숫자의 합을 출력합니다.
print(str1_int + str2_int)
