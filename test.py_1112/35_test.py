# 반복문으로 피라미드 만들기(1)
output = ""

for i in range(1, 10):
    for j in range(0, i):
        output += "*"
    output += "\n"

print(output)