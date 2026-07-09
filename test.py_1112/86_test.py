import random

# 랜덤한 이름 생성용
hanguls = list("가나다라마바사아자차카타파하")

# 파일 쓰기
with open("info.txt", "w", encoding="utf-8") as file:
    for i in range(1000):
        # 랜덤한 값 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        # 파일에 저장
        file.write("{}, {}, {}\n".format(name, weight, height))