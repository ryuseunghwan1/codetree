a, b = map(int, input().split())

# 정수 부분
integer = a // b
remainder = a % b

# 소수 부분 21자리 만들기
decimal_part = ""

for _ in range(21):
    remainder *= 10
    digit = remainder // b
    decimal_part += str(digit)
    remainder %= b

print(f"{integer}.{decimal_part}")