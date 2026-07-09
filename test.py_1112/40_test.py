# break 키워드
# 변수를 반복합니다.
i = 0

# 무한 반복합니다.
while True:
    # 몇 번쨰 반복인지 출력합니다.
    print("{}번째 반복문입니다.".format(i))
    # 반복을 종료합니다.
    input_text= input("> 종료하시겠습니까?(y/n): ")
    if input_text in ["y", "y"]:
        break