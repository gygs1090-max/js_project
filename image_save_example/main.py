from urllib import request

image_url = "https://www.hanbit.co.kr/images/common/logo_hanbit.png"
save_file_name = "01_output.png"

target = request.urlopen(image_url)
output = target.read()

with open(save_file_name, "wb") as file:
    file.write(output)

print("이미지 저장이 완료되었습니다.")
