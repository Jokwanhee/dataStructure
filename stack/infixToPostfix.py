'''
중위표기식 --> 후위표기식 변환

example
1) A + B * C
    []
    [] A
    ['+'] A
    ['+'] AB
    ['+','*'] AB --> 연산자들의 우선순위 고려, '+'가 '*'보다 우선순위가 낮기 때문에 '+'위에 '*'를 삽입한다.(스택, 후입선출)
    ['+','*'] ABC
    ['+'] ABC*
    [] ABC*+

2) A * B + C
            []
   A        [] A
   A*       ['*'] A
   A*B      ['*'] AB
   A*B+     ['+'] AB*
   A*B+C    ['+'] AB*C
   A*B+C    [] AB*C+

3) (A + B) * C
   D        []
   (        ['(']
   (A       ['('] A
   (A+      ['(','+'] A
   (A+B     ['(','+'] AB
   (A+B)    [] AB+
   (A+B)*   ['*'] AB+
   (A+B)*C  ['*'] AB+C
   (A+B)*C  [] AB+C*

조건
1. 입력된 중위표기 수식을 순서대로 하나씩 스캔한다.
2. 피연산자를 만나면 바로 (후위표기 수식으로) 출력한다.
3.  연산자를 만나면 어딘가에 잠시 저장해야 한다.
    후위표기에서는 연산자가 피연산자들 뒤에 나오기 때문이다.
    따라서 적절한 위치를 찾을 때까지 출력을 보류하여야 한다.
    연산자의 저장에는 스택이 사용된다.
'''
from LIFO import Stack
from postfixCalculate import postfixCaculator


def precedence(op):  # 연산자 우선순위
    if op == "(" or op == ")":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == '/':
        return 2
    else:
        return -1


def infixToPostfix(expr: list):  # 중위표기식 -> 후위표기식 변환
    s = Stack()
    output = []  # 후위표기식 리스트
    for ch in expr:
        if ch == "(":
            s.push(ch)
        elif ch == ")":
            while not s.isEmpty():
                op = s.pop()
                if op == "(":
                    break
                else:
                    output.append(op)
        elif ch in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(ch) <= precedence(op):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(ch)
        else:
            output.append(ch)

    while not s.isEmpty():
        output.append(s.pop())

    return output


expression1 = ["8", "/", "2", "-", "3", "+", "(", "3", "*", "2", ")"]
expression2 = ["1", "/", "2", "*", "4", "*", "(", "1", "/", "4", ")"]
print(infixToPostfix(expression1))
print(infixToPostfix(expression2))
print(postfixCaculator(infixToPostfix(expression1)))
print(postfixCaculator(infixToPostfix(expression2)))
