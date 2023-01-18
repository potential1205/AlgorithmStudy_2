from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(queue):
    visit,day = [[False for j in range(m)] for i in range(n)], 0
    while queue:
        gy,gx,level = queue.popleft()
        day = max(day,level)
        visit[gy][gx] = True
        for i in range(4):
            ky,kx = gy+dy[i],gx+dx[i]
            if ky<0 or kx<0 or ky>=n or kx>=m or visit[ky][kx] == True or board[ky][kx] == -1:
                continue

            if board[ky][kx] == 0:
                board[ky][kx] = 1
                queue.append([ky,kx,level+1])
                visit[ky][kx] = True
                
            elif board[ky][kx] == 1:
                queue.append([ky,kx,level+1])
                visit[ky][kx] = True
        
    return day


if __name__ == "__main__":
    m,n = map(int,input().split())

    board,flag = [],0  
    for i in range(n):
        line = list(map(int,input().split()))
        board.append(line)
        for x in line:
            if x==0:
                flag=1
                break
    if flag==0:
        print(0)
        exit()

    queue,blank = deque(),0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append([i,j,0])

    day = bfs(queue)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print(-1)
                exit()
    
    print(day)