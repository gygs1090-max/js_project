#  "from test_package import *" 로
# 모듈을 읽어 들이 때 까지 가져올 모듈

__all__ = ["module_a", "module_b"]
# 사용 시 읽어 들일 모듈의 목록

# 패키지를 읽어 들일 때 처리를 작성할 수 있습니다..
print("test_package를 읽어 들였습니다.")
