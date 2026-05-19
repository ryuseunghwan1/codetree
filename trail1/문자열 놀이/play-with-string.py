# 1. 초기 문자열 S와 질의의 수 Q를 입력받습니다.
S, Q = input().split()
Q = int(Q)

# 문자열을 수정할 수 있도록 리스트로 변환합니다.
s_list = list(S)

# 2. Q개의 질의를 순서대로 처리합니다.
for _ in range(Q):
    query = input().split()
    q_type = query[0]
    
    if q_type == '1':
        # [타입 1] a번째 문자와 b번째 문자를 교환합니다.
        # 파이썬 인덱스는 0부터 시작하므로 입력값에서 1을 빼줍니다.
        a = int(query[1]) - 1
        b = int(query[2]) - 1
        
        # 두 위치의 문자를 서로 바꿉니다.
        s_list[a], s_list[b] = s_list[b], s_list[a]
        
    elif q_type == '2':
        # [타입 2] 문자 x를 전부 문자 y로 변경합니다.
        x = query[1]
        y = query[2]
        
        # 리스트를 처음부터 끝까지 돌며 x를 찾아서 y로 교체합니다.
        for i in range(len(s_list)):
            if s_list[i] == x:
                s_list[i] = y
                
    # 하나의 질의가 끝날 때마다 현재 문자열 상태를 합쳐서 출력합니다.
    print(''.join(s_list))