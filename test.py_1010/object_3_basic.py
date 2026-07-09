# 학생 만들기, 총점 계산, 평균 계산, 출력 문자열 만들기까지 함수로 뺌.
#  객체를 처리하는 함수(2)
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }
#  학생을 처리하는 함수를 선언합니다.
def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]


def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

# 학생 리스트를 선언합니다.
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
]
# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 출력합니다.
    print(student_to_string(student))

# 같은 결과를 내지만 코드를 역할별로 더 잘 나눈 버전입니다. 나중에 총점 계산 방식이나 출력 형식을 바꾸고 싶을 때 함수 하나만 수정하면 돼서 관리하기가 더 쉽습니다.
