# 순환 알고리즘 - 하노이의 탑
"""
A |  B |  C |
  |    |    |
  |    |    |
 ---  ---  ---
1) 먼저 위에 쌓여 있는 n-1개의 원판을 B로 옮긴다. C를 임시막대로 사용
2) 이제 제일 밑에 있는 원판을 바로 C로 옮긴다.
3) B로 옮겨져 있는 n-1개의 원판을 C로 옯긴다. A를 임시막대로 사용한다.
"""

# 하노이의 탑 - 순환 방법
def recursion_hanoi(n, fr, tmp, to):
    if (n==1):
        print("원판 1: %s --> %s"%(fr,to)) # 맨 위 한 원판, A->C
    else:
        recursion_hanoi(n-1, fr, to, tmp) # n-1개, A->B
        print("원판 %d: %s --> %s"%(n,fr,to))
        recursion_hanoi(n-1, tmp, fr, to) # n-1개, B->C

def main():
    _input = int(input("하노이 탑의 원판 개수를 입력하시오 : "))
    recursion_hanoi(_input, "A", "B", "C")

if __name__ == '__main__':
    main()