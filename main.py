from dfscount import *


def trio():
    c = int(input())
    for _ in range(c):
        h, w = map(int, input().split())
        board = []
        for i in range(h):
            board.append([])
            row_str = input()
            for j in row_str:  # 문자열 내의 각 문자를 검은 칸(1)과 흰 칸(0)으로 바꾸어 board에 append
                if j == '#':
                    board[-1].append(1)
                elif j == '.':
                    board[-1].append(0)
                else:
                    pass
        count = cover(board)  # dfscount 모듈의 함수를 호출
        print(count)


if __name__ == "__main__":
    trio()



