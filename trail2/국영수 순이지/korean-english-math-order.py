n = int(input())

students = []

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    students.append(Student(name, int(kor), int(eng), int(math)))

students.sort(key= lambda x : (-x.kor, -x.eng, -x.math))

for i in students:
    print(i.name, i.kor, i.eng, i.math)
