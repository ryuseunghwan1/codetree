secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class secret:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

my_secret = secret(secret_code, meeting_point, time)

print('secret code :', my_secret.secret_code)
print('meeting point :', my_secret.meeting_point)
print('time :', my_secret.time)