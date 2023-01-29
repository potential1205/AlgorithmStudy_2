from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(board,i,j,visit,l,r):
    queue = deque([[i,j]])
    positions = [[i,j]]

    while queue:
        y,x = queue.popleft()
        visit[y][x] = True
        for i in range(4):
            ky,kx = y+dy[i], x+dx[i]
            if ky <0 or ky>=n or kx <0 or kx >= n or visit[ky][kx] == True or abs(board[y][x]-board[ky][kx]) < l or abs(board[y][x]-board[ky][kx]) > r: 
                continue

            queue.append([ky,kx])
            visit[ky][kx] = True
            
            positions.append([ky,kx])
    
    return positions,visit
    
if __name__ == "__main__":
    n,l,r = map(int,input().split())
    board = [list(map(int,input().split())) for i in range(n)]
    day = 0
    
    while True:
        flag = 0
        visit = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if visit[i][j] == False:
                    positions,visit = move(board,i,j,visit,l,r)
                    leng = len(positions)

                    if leng > 1:
                        flag=1
                        avg = sum([board[y][x] for y, x in positions]) // leng
                        for y,x in positions:
                            board[y][x] = avg
        if flag==0:
            print(day)
            break
        day+=1
