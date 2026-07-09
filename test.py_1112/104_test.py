# 시간 처리하기

# 모듈을 읽어 들입니다.

import datetime
now = datetime.datetime.now()

# 특정 시간 이후의 시간 구하기
print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(weeks=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

# 특정 시간 이전의 시간 구하기
print("# datetime.timedelta로 시간 빼기")
before = now - datetime.timedelta(days=1)
print(before.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

