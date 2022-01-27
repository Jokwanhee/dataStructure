# 순환 알고리즘 - 거듭제곱
import time


# 순환 거듭제곱
def recursionPower(x, n):
    if (n == 0):
        return 1
    elif (n % 2):  # n승이 홀수
        return x * recursionPower(x * x, (n - 1) // 2)
    else:  # n승이 짝수
        return recursionPower(x * x, n // 2)


# 반복 거듭제곱
def repeatPower(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


def main():
    _inputX = int(input("x을 입력하시오 : "))
    _inputN = int(input("n을 입력하시오 : "))
    start_recursion = time.time()
    print("순환 알고리즘 순환 거듭제곱, %d의 %d제곱 :" % (_inputX, _inputN), recursionPower(_inputX, _inputN))
    end_recursion = time.time()
    print("순환 알고리즘 순환 거듭제곱 소요시간 :", end_recursion - start_recursion)
    start_repeat = time.time()
    print("순환 알고리즘 반복 거듭제곱, %d의 %d제곱 :" % (_inputX, _inputN), repeatPower(_inputX, _inputN))
    end_repeat = time.time()
    print("순환 알고리즘 반복 거듭제곱 소요시간 :", end_repeat - start_repeat)

if __name__ == '__main__':
    main()
