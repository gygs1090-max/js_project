# 매개변수로 받은 함수를 10번 호출하는 함수

def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수

def print_hello():
    print("안녕하세요")

# 조합하기
call_10_times(print_hello)

# 프로그램을 실행하면 print_hello() 함수를 10번 실행함. 
# 따라서 "안녕하세요" 라는 문자열을 10번 출력함.