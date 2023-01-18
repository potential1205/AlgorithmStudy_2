from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x,visit,target):
    queue = deque([[y,x]])
    cnt=1
    while queue:
        y,x = queue.popleft()
        visit[y][x] = True
        for i in range(4):
            ky,kx = y+dy[i], x+dx[i]
            if ky < 0 or kx <0 or ky>=n or kx>=m or visit[ky][kx] == True or board[ky][kx]!=target:
                continue

            queue.append([ky,kx])
            visit[ky][kx] = True
            cnt+=1
    
    return visit,cnt*cnt

if __name__ == "__main__":

    m,n = map(int,input().split())
    board = [input() for _ in range(n)]

    white, blue = [], []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'W':
                white.append([i,j])
            elif board[i][j] == 'B':
                blue.append([i,j])
    
    visit = [[False for j in range(m)] for i in range(n)]
    white_sum, blue_sum = 0,0
    for y,x in white:
        if visit[y][x] == False:
            visit,val = bfs(y,x,visit,'W')
            white_sum+=val
    
    visit = [[False for j in range(m)] for i in range(n)]
    for y,x in blue:
        if visit[y][x] == False:
            visit,val = bfs(y,x,visit,'B')
            blue_sum+=val
    print("{} {}".format(white_sum,blue_sum))
    