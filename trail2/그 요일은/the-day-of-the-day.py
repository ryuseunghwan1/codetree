m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

# 1. 2024년 각 달의 마지막 날짜 (윤년이므로 2월은 29일)
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 2. 1월 1일부터 해당 날짜까지 총 며칠이 걸리는지 계산하는 함수
def count_days(m, d):
    total_days = 0
    # 1월부터 (m-1)월까지의 일수를 모두 더함
    for i in range(1, m):
        total_days += num_of_days[i]
    # 이번 달의 일수(d)를 더함
    total_days += d
    return total_days

# 3. 두 날짜가 1월 1일 기준으로 각각 며칠째인지 구함
start_total = count_days(m1, d1)
end_total = count_days(m2, d2)

# 두 날짜 사이의 총 일수 (시작일과 종료일 포함)
# 예: 2월 5일부터 2월 5일까지는 0일이 지난 것이지만, 당일 하루가 포함되므로 차이값에 +1을 생각해야 합니다.
elapsed_days = end_total - start_total

# 4. 요일을 숫자로 매칭 (시작일인 m1월 d1일이 '월요일'이므로 Mon을 0으로 설정)
day_to_num = {
    "Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6
}
target_num = day_to_num[target_day]

# 5. 시작일부터 하루씩 넘기며 target_day가 몇 번 나오는지 카운트
ans = 0
# i는 시작일(0)부터 경과한 일수(elapsed_days)까지 반복
for i in range(elapsed_days + 1):
    # 시작일이 월요일(0)이므로, i일이 지난 후의 요일 숫자는 (0 + i) % 7 입니다.
    current_day_num = i % 7
    
    if current_day_num == target_num:
        ans += 1

print(ans)