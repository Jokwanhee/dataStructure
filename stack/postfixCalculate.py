'''
스택의 응용 : 수식의 계산
"계산기"
    전위(prefix) : 연산자 피연산자1 피연사자2 --> + A B
    중위(infix) : 피연산자1 연산자 피연산자2 --> A + B
    후위(postfix) : 피연산자1 피연산자2 연산자 --> A B +

후위표기 수식의 계산 example
82/3-32*+
1) 8 / 2 = 4 --> 43-32*+
2) 4 - 3 = 1 --> 132*+
3) 3 * 2 = 6 --> 16+
4) 1 + 6 = 7 --> 7

조건
1. 수식을 왼쪽 -> 오른쪽 스캔
2. 피연산자가 나오면 무조건 스택에 저장
3. 연산자가 나오면 스택에서 피연산자 두 개를 꺼내 연산을 실행
4. 그 결과를 다시 스택에 저장
'''
from LIFO import Stack


def postfixCaculator(myList: list): # 후위 표기식 수식의 계산
    s = Stack()
    for ch in myList:
        if ch in ("+", "-", "*", "/"):
            val2 = s.pop()
            val1 = s.pop()
            if ch == "+":
                s.push(val1 + val2)
            elif ch == "-":
                s.push(val1 - val2)
            elif ch == "*":
                s.push(val1 * val2)
            elif ch == "/":
                s.push(val1 / val2)
        else:
            s.push(float(ch))

    return s.peek()

expression1 = ["8", "2", "/", "3", "-", "3", "2", "*", "+"]
expression2 = ["1", "2", "/", "4", "*", "1", "4", "/", "*"]
