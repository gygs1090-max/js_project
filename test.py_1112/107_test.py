# urllib 모듈

from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output.decode("utf-8"))
