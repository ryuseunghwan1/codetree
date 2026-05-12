unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

fix = Bomb(unlock_code, wire_color, seconds)

print('code :', fix.code)
print('color :', fix.color)
print('second :', fix.second)