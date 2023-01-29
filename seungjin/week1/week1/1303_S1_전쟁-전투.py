from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(y,x,type):
    col=1
    queue=deque()
    queue.append((y,x))
    graph[y][x]='V'
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if graph[ny][nx]!=type:
                continue
            if graph[ny][nx]==type:
                queue.append((ny,nx))
                graph[ny][nx]='V'
                col+=1
    return col**2

n,m=map(int,input().split())
graph=[]
B_total=0
W_total=0

for i in range(m):
    graph.append(list(input()))

for i in range(m):
    for j in range(n):
        if graph[i][j]=='W':
            collegue=bfs(i,j,'W')
            W_total+=collegue
        elif graph[i][j]=='B':
            collegue=bfs(i,j,'B')
            B_total+=collegue
        print(W_total,B_total)
print(W_total,B_total)