#  모든 예외 잡기

# 변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]
# try except 구문으로 예외를 처리합니다.
try:
    # 숫자를 입력받습니다.
    number_input = int(input("정수 입력> "))
    # 리스트의 요소를 출력합니다.
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    # ValueError가 발생하는 경우.
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError as exception:
    # IndexError가 발생하는 경우.
    print("리스트의 인덱스를 벗어났습니다!")
    print(type(exception), exception)
except Exception as exception:
    # ValueError, IndexError가 아닌 예외가 발생했을 때 실행됨.
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)
