n = int(input())

class Student:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

students = []

for i in range(1, n+1):
    a, b = map(int, input().split())
    c = i
    cnt = Student(a, b), c
    students.append(cnt)

students.sort(key= lambda x: (x[0].height, -x[0].weight))

for j in students:
    print(j[0].height, j[0].weight, j[1])