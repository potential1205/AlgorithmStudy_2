from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def rotate(board):
    return list(map(list, zip(*board)))[::-1]

def gravity(board):
    for _ in range(n-1):
        for i in range(n-2,-1,-1):
            for j in range(n):
                if board[i][j] == -1 or board[i][j] == -2:
                    continue
                else:
                    if board[i+1][j] == -2:
                        board[i+1][j] = board[i][j]
                        board[i][j] = -2
    return board


def remove_block(board,top_priority_group_info):
    cnt=0
    for y,x in top_priority_group_info[4]:
        board[y][x] = -2
        cnt+=1
    return board,cnt**2


def bfs(board,sy,sx,type,visit):
    queue = deque([[sy,sx]])
    total_group_cnt, rainbow_cnt = 0, 0

    position = []
    rainbow_position = []

    while queue:
        y,x = queue.popleft()
        visit[y][x] = True
        total_group_cnt +=1
        position.append([y,x])

        if board[y][x] == 0:
            rainbow_cnt+=1
            rainbow_position.append([y,x])

        for i in range(4):
            ky,kx = y+dy[i], x+dx[i]
            if ky<0 or kx<0 or ky>=n or kx>=n or visit[ky][kx] == True or board[ky][kx] == -1 or board[ky][kx] == -2:
                continue
            
            if board[ky][kx] == 0 or board[ky][kx] == type:
                queue.append([ky,kx])
                visit[ky][kx] = True

    for i,j in rainbow_position:
        visit[i][j] = False

    return total_group_cnt,rainbow_cnt,visit,position


def get_info(board):
    visit = [[False for j in range(n)] for i in range(n)]
    group_info = []
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False and board[i][j] != -1 and board[i][j] != 0 and board[i][j] != -2:
                total_group_cnt,rainbow_cnt,visit,position = bfs(board,i,j,board[i][j],visit)
                if total_group_cnt>=2:
                    group_info.append([total_group_cnt,rainbow_cnt,i,j,position])

    if len(group_info) > 0:
        group_info.sort(key = lambda x : (-x[0],-x[1],-x[2],-x[3]))
        return False, group_info[0]
    else:
        return True, 0


def solve(board):
    total_score = 0
    while True:
        end, top_priority_group_info = get_info(board)
        if end: break
        board, score = remove_block(board,top_priority_group_info)
        board = gravity(board)
        board = rotate(board)
        board = gravity(board)
        total_score += score

    return total_score


if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for i in range(n)]
    print(solve(board))
    
    
