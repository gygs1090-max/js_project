# __str__() 함수 정의하기

#  클래스를 선언합니다.

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
             self.english + self.science

    def get_average(self):
        return self.get_sum() / 4
# __str__() 함수를 (선언)정의합니다.
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

# 학생 리스트를 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
]

# 출력합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    #  str() 함수를 호출합니다. 즉, __str__() 함수를 호출됩니다.
    print(str(student))
