# 순환 알고리즘 - 팩토리얼
# n! = 1 ... (n = 1)
#    = n*(n-1)! ... (n > 1)

# 팩토리얼 순환 구조, O(n)
def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n-1)

# 팩토리얼 반복 구조, O(n)
def factorialRepeat(n):
    result = 1
    if (n > 1):
        for i in range(n, 0 , -1):
            result = result * i
    return result

def main():
    _input = int(input("n을 입력하시오 : "))
    print("팩토리얼 순환 구조 :", factorial(_input))
    print("팩토리얼 반복 구조 :", factorialRepeat(_input))

if __name__ == "__main__":
    main()

