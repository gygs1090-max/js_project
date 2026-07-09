# info.txt 파일 읽어서 BMI 계산하기

with open("info.txt", "r", encoding="utf-8") as file:
    for line in file:
        # 이름, 몸무게, 키 분리
        (name, weight, height) = line.strip().split(", ")

        # 데이터가 비어 있으면 건너뛰기
        if (not name) or (not weight) or (not height):
            continue

        # BMI 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)

        # BMI 판정
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상 체중"
        else:
            result = "저체중"

        # 결과 출력
        print('\n'.join([
            "이름: {}",
            "몸무게: {}kg",
            "키: {}cm",
            "BMI: {:.2f}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))

        print("-" * 30)