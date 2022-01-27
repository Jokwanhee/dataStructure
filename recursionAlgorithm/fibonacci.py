# 순환 알고리즘 - 피보나치 수열
"""
         0, n = 0
fib(n) = 1, n = 1
         fib(n-2) + fib(n-1), n > 1
"""
import time


# 피보나치 수열 - 순환 방법
def recursion_fibo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return recursion_fibo(n - 2) + recursion_fibo(n - 1)


# 피보나치 수열 - 반복 방법
def repeat_fibo(n):
    if (n < 2): return n
    last = 0
    current = 1
    for i in range(2, n + 1):
        tmp = current
        current += last
        last = tmp
    return current


def main():
    _input = int(input("n을 입력하시오 : "))
    start_recursion = time.time()
    print("피보나치 수열 - 순환 방법 :", recursion_fibo(_input))
    end_recursion = time.time()
    print("피보나치 수열 - 순환 소요시간 :", end_recursion - start_recursion)
    start_repeat = time.time()
    print("피보나치 수열 - 반복 방법 :", repeat_fibo(_input))
    end_repeat = time.time()
    print("피보나치 수열 - 반복 소요시간 :", end_repeat - start_repeat)


if __name__ == '__main__':
    main()
