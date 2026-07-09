# 조건을 활용한 리스트 내포

# 리스트를 선언합니다.
array = ["사과","자두","초콜릿","바나나","제리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

# 출력합니다.
print(output)