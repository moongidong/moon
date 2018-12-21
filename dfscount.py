rel_coord = (((0, 0), (1, 0), (0, 1)), ((0, 0), (0, 1), (1, 1)), ((0, 0), (1, 0), (1, 1)), ((0, 0), (1, 0), (1, -1)))


def put_triomino(y, x, pos, sign, board):  # board의 게임판에서 트리오미노를 (x, y) 좌표를 기준으로 pos에 해당하는 상대 위치로 놓거나(sign == 1) 들어낸다.(sign == -1)
    global rel_coord
    h, w = len(board), len(board[0])
    res = True
    for i in range(3):  # 트리오미노의 각 칸에 대해 iterate
        abs_y = y + rel_coord[pos][i][0]
        abs_x = x + rel_coord[pos][i][1]
        if abs_x < 0 or abs_x >= w or abs_y < 0 or abs_y >= h:  # 게임판 이탈
            res = False
        else:
            board[abs_y][abs_x] += sign
            if board[abs_y][abs_x] > 1:  # 겹침
                res = False
    return res


def cover(board):
    h, w = len(board), len(board[0])
    y, x = -1, -1
    for i in range(h):  # 위에서부터 탐색
        for j in range(w):  # 왼쪽부터 탐색
            if not board[i][j]:  # 빈 칸 발견 후 break
                y = i
                x = j
                break
        if y >= 0:
            break

    if y == -1:  # 발견 못 했다면 게임판 완성, 1 반환
        return 1
    ret = 0
    for type in range(4):  # 4가지의 가능한 방법으로 트리오미노를 놓아 본다.
        if put_triomino(y, x, type, 1, board):  # 성공했을 경우 재귀한다.
            ret += cover(board)
        put_triomino(y, x, type, -1, board)  # 놓았던 트리오미노는 다시 들어낸다.

    return ret
