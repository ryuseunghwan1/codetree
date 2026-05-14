m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

wkd = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

# 1월 1일부터 m1월 d1일까지의 총 일수 계산 함수
def get_total_days(m, d):
    total = d
    for i in range(1, m):
        total += month[i]
    return total

total_1 = get_total_days(m1, d1)
total_2 = get_total_days(m2, d2)

# 두 날짜의 차이 (m2월 d2일 - m1월 d1일)
diff = total_2 - total_1

# 파이썬의 % 연산자는 음수도 요일 리스트 범위 안으로 잘 순환시켜줍니다.
# 예를 들어 diff가 -1이면 (일요일 방향), wkd[-1 % 7] -> wkd[6] (Sun)이 됩니다.
print(wkd[diff % 7])