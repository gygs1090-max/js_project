# 재귀 함수로 구현한 피보나치 수열

# 변수를 선언합니다.
counter = 0

# 함수를 선언합니다.
def fibonacci(n):
    global counter
    counter += 1

    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 함수를 호출합니다.
fibonacci(10)
print("---")
print("fibonacci(10) 계산할 때 함수를 호출한 횟수는 {}번입니다.".format(counter))