'''
"미로에 빠진 생쥐를 구출하라"
- 스택을 이용한 깊이우선탐색(DFS)
*DFS : Depth First Search

미로 --> 2차원 배열 구조 (2차원 리스트)
    --> 6 x 6 미로(36칸)
    --> 1 (미로의 벽)
    --> 0 (미로에서 갈 수 있는 경로)
    --> e (생쥐의 위치) (x,y / 열,행)
    --> x (출구)
    --> 탐색 순서 (상->하->좌->우) ... 탐색 순서가 "좌우상하"라면 또 달라진다.

탐색 알고리즘
1) 탐색 함수와 깊이 우선 탐색의 함수를 만든다.
2) 시작위치를 스택에 넣는다. 현재 스택에는 시작위치만 들어 있다.
3) 스택이 공백이 아니면 하나의 위치를 꺼낸다. 이것이 현재위치이다.
4) 꺼낸 위치가 "x"이면 True 반환 아니면 "x"일 때 까지 반복
5) 지나온 위치는 무언의 표시를 해둔다. ex) "." 표시
6) 탐색 함수를 사용하여 탐색의 순서는 우: 1순위, 좌: 2순위, 하: 3순위, 상: 4순위 (변동 가능)
7) 깊이 우선 탐색의 함수 마지막은 False를 반환한다. 이유는 함수 내부에서 반복문을 사용하였을 때, "x" 위치를 만나지 못하면
    True 반환을 하지 않고 반복문을 빠져나온다. 이를 False로 반환하여 미로탐색의 실패를 알릴 수 있다.

'''
from LIFO import Stack

map = [["e", "1", "1", "1", "1", "1"],
       ["0", "0", "0", "0", "0", "1"],
       ["1", "0", "1", "0", "1", "1"],
       ["1", "1", "1", "0", "0", "x"],
       ["1", "1", "1", "0", "1", "1"],
       ["1", "1", "1", "1", "1", "1"]]
MAX_SIZE = 6


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAX_SIZE or y >= MAX_SIZE:
        return False
    else:
        return map[x][y] == '0' or map[x][y] == "x"


def DFS():
    s = Stack()
    s.push((0, 0))
    print("DFS: ")
    while not s.isEmpty():
        here = s.pop()
        print(here, end=" -> ")
        (x, y) = here
        if map[x][y] == "x":
            return True
        else:
            map[x][y] = '.'
            if isValidPos(x - 1, y):
                s.push((x - 1, y))  # 상 - 4
            if isValidPos(x + 1, y):
                s.push((x + 1, y))  # 하 - 3
            if isValidPos(x, y - 1):
                s.push((x, y - 1))  # 좌 - 2
            if isValidPos(x, y + 1):
                s.push((x, y + 1))  # 우 - 1
        print("현재 스택: ", s.items)
    return False


if __name__ == '__main__':
    result = DFS()
    if result:
        print("미로탐색 성공")
    else:
        print("미로탐색 실패")
