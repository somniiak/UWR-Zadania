from wdi import *

def prArr(arr):
    global n
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=',')
        print()

def sqArray(n):
    arr = Array(n)
    for i in range(n):
        arr[i] = Array(n)
        for j in range(n):
            arr[i][j] = -1
    return arr

def is_valid_move(x, y, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def knight_move(n, x, y, move_count):
    if move_count == n * n:
        return True
    
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)] # 8
    
    for i in range(8):
        dx, dy = moves[i]
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, n):
            board[nx][ny] = move_count
            if knight_move(n, nx, ny, move_count + 1):
                return True
            board[nx][ny] = -1  # Cofnij ruch (backtracking)

def knight(n, start_x, start_y, board):
    board[start_x][start_y] = 0
    if knight_move(n, start_x, start_y, 1):
        return board
    else:
        return False

n = 3
board = sqArray(n)

x = knight(n, 0, 0, board)
prArr(x)