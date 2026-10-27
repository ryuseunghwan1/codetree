user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Users:
    def __init__(self, id = 'codetree', level = 10):
        self.id = id
        self.level = level

user1 = Users()
user2 = Users(user2_id, user2_level)

print('user', user1.id, 'lv', user1.level)
print('user', user2.id, 'lv', user2.level)