from collections import deque

def rotate(direc,index):
    
    if index == 'L':
        direc-=1
    elif index == 'D':
        direc+=1
    
    if direc == 4:
        direc = 0
    
    if direc == -1:
        direc = 3
    return direc 
        

def solve(board,info,l):
    time, direction,cnt = 1, 1, 0
    snake = deque([[0,0]])

    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[0][0] = True

    while True:
        y,x = snake[-1][0],snake[-1][1]
        if direction == 0:
            ky,kx = y-1, x
        elif direction == 1:
            ky,kx = y, x+1
        elif direction == 2:
            ky,kx = y+1, x
        elif direction == 3:
            ky,kx = y, x-1
        
        if ky<0 or kx<0 or ky>=n or kx>=n or visit[ky][kx]==True:
            break
            
        snake.append([ky,kx])
        visit[ky][kx] = True

        if board[ky][kx] == 1:
            board[ky][kx] = 0
        elif board[ky][kx] == 0:
            ny,nx = snake.popleft()
            visit[ny][nx] = False

        if cnt!=l and info[cnt][0] == time:
            direction = rotate(direction,info[cnt][1])
            cnt+=1

        time+=1
                
    return time


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    
    board = [[0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        y,x = map(int,input().split())
        board[y-1][x-1] = 1
    
    l = int(input())
    info = []
    for _ in range(l):
        x,c = map(str,input().split())
        info.append([int(x),c])

    print(solve(board,info,l))