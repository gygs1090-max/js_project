# 클래스를 선언합니다.

class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls): # student 클래스의에 print 함수를 구현합니다.
        print("----- 학생 목록 -----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(student.to_string()) # student.student 라고 해도 상관없지만, 여기서는 매개변수로 받은 cls를 사용합니다.
        print("----- 현재 총 학생 수는 {}명입니다. -----".format(cls.count))
        print("--------------------------------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
             self.english + self.science

    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):

        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

# 학생 리스트를 선언합니다.

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 55, 72, 78)

# 현재 생성된 학생을 모두 출력합니다.
Student.print()
