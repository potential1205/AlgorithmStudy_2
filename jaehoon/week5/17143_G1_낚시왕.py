# dy = [-1, 1, 0, 0]                                                                    
# dx = [0, 0, -1, 1]

# def move(board):                                                             
#     temp_board = [line[:] for line in board]
#     for i in range(row):
#         for j in range(col):
#             if board[i][j]:
#                 z,s,d = board[i][j][0]
#                 y,x = i,j
#                 if d == 1 or d == 2:
#                     move_size = s % (row*2-2)
#                 elif d == 3 or d == 4:
#                     move_size = s % (col*2-2)
                
#                 while move_size > 0:
#                     if d == 1 and y == 0:
#                         d = 2
#                     elif d == 2 and y == row:
#                         d = 1
#                     elif d == 3 and x == col:
#                         d = 4
#                     elif d == 4 and x == 0:
#                         d = 3
                    
#                     if d == 1:
#                         y = i-1
#                     elif d == 2:
#                         y = i+1
#                     elif d == 3:
#                         x = j+1
#                     elif d == 4:
#                         x = j-1
                    
#                     move_size-=1
                
#                 board[y%row][x%col].append([z,s,d])

#     return board


# def hunt(board,time):
#     size = 0
#     for i in range(row):
#         if board[i][time]:
#             value = board[i][time][0]
#             size = value[0]
#             board[i][time].remove(value)
#             break

#     return size


# def solve(board):
#     total_size = 0
#     for time in range(col):
#         total_size += hunt(board,time)
#         board = move(board)

#     return total_size

# if __name__ == "__main__":
#     row,col,num = map(int,input().split())
#     board = [[[] for j in range(col)] for i in range(row)]
#     for i in range(num):
#         r,c,s,d,z = map(int,input().split())
#         board[r-1][c-1].append([z,s,d])
#     print(solve(board))


import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def fish(j):
    for i in range(R):
        if board[i][j]:
            x = board[i][j][2]
            board[i][j] = 0
            return x
    return 0


def move():
    global board  # board[i][j] 안에는 (s,d,z)의 값이 들어있음. 상어가 없는 경우엔 0이 들어있음
    new_board = [[0 for _ in range(C)] for _ in range(R)]  # 상어들의 새 위치를 담을 공간
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                # 이 상어의 다음 위치는
                ni, nj, nd = get_next_loc(i, j, board[i][j][0], board[i][j][1])
                if new_board[ni][nj]:
                    new_board[ni][nj] = max(
                        new_board[ni][nj],
                        (board[i][j][0], nd, board[i][j][2]),
                        key=lambda x: x[2],
                    )
                else:
                    new_board[ni][nj] = (board[i][j][0], nd, board[i][j][2])

    board = new_board  # board가 이제 상어들의 새 위치를 가리키도록


def get_next_loc(i, j, speed, dir):

    if dir == UP or dir == DOWN:  # i
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, UP)
        return (speed, j, DOWN)

    else:  # j
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, LEFT)
        return (i, speed, RIGHT)


UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    board[r][c] = (s, d, z)
    # s : speed
    # d : 1(up), 2(down), 3(right), 4(left)
    # z : size


ans = 0
for j in range(C):
    ans += fish(j)
    move()

print(ans)