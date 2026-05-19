N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# 학생들의 벌칙 횟수를 기록할 배열 (1번부터 N번까지이므로 N+1 크기)
penalty_count = [0] * (N + 1)

# 최초로 벌금을 내는 학생을 찾았는지 여부를 체크할 변수
found = False

# 벌칙을 순서대로 확인하면서 실시간으로 누적
for s_num in student:
    penalty_count[s_num] += 1
    
    # 벌칙을 받은 직후, 해당 학생의 벌칙 횟수가 K번 이상이 되었는지 확인
    if penalty_count[s_num] >= K:
        print(s_num)
        found = True
        break  # 최초의 학생을 찾았으므로 반복문 탈출

# M번의 벌칙이 다 끝날 때까지 벌금을 내는 학생이 없다면 -1 출력
if not found:
    print(-1)