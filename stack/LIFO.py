'''
스택은 후입선출 (Last-In First Out: LIFO)
응용
1. 되돌리기(undo)
2. 함수 호출에서 복귀주소
3. 괄호 닫기
4. 계산기 프로그램
'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # items, 빈 리스트 인지 아닌지
        return len(self.items) == 0

    def push(self, e):  # items, 맨 후단에 값 추가
        self.items.append(e)

    def pop(self):  # items, 맨 후단에 값 삭제0
        if not self.isEmpty():
            return self.items.pop(-1)

    def peek(self):  # items, 맨 후단에 값 표시
        if not self.isEmpty():
            return self.items[-1]

    def size(self):  # items의 길이
        return len(self.items)

    def clear(self):  # items 초기화
        if not self.isEmpty(): self.items = []
        return self.items

