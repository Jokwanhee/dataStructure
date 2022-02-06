'''
스택의 응용 : 괄호 검사
조건 1 : if ((i=0) && (j==0) --> 위반
조건 2 : while (it<10)) { it--; } --> 위반
조건 3 : A[(i+1])=0; --> 위반
'''
# (a+{b+c}) = b
from LIFO import Stack


def checkBracket(inputText: str):
    s = Stack()
    for ch in inputText:
        if ch in ("(", "{", "["):
            s.push(ch)
        else:
            if ch in (")", "}", "]"):
                if s.isEmpty():
                    return False  # 조건 2 위반
                else:
                    left = s.pop()
                    if (ch == ")" and left != "(") or \
                            (ch == "}" and left != "{") or \
                            (ch == "]" and left != "]"):
                        return False  # 조건 3 위반
    return s.isEmpty()  # False --> 조건 1 위반


myStr = ("{A[(i+1)]=0;}", "if ((i==0) && (j==0)", "while (it<10)) {it--;}", "A[(i+1])=0;")
for i in myStr:
    result = checkBracket(i)
    print(i, "-->", result)
