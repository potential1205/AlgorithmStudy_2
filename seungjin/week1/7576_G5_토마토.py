from collections import deque
m,n=map(int,input().split())
graph=[]
start_l=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
check=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            start_l.append((i,j))
#print(start_l)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    visited[y][x]=True
    while queue:
        y,x=queue.popleft()
        if x+1 < m and x+1 >=0 and y>=0 and y<n and graph[y][x+1]!=1 and graph[y][x+1]!=-1 and visited[y][x+1]==False:
            check=1
            queue.append((y,x+1))
            visited[y][x+1]=True
            if graph[y][x+1]==0 or graph[y][x+1]>graph[y][x]+1:
                graph[y][x+1]=graph[y][x]+1
        if x-1 < m and x-1 >=0 and y>=0 and y<n and graph[y][x-1]!=1 and graph[y][x-1]!=-1 and visited[y][x-1]==False:
            check=1
            queue.append((y,x-1))
            visited[y][x-1]=True
            if graph[y][x-1]==0 or graph[y][x-1]>graph[y][x]+1:
                graph[y][x-1]=graph[y][x]+1
        if x < m and x >=0 and y+1>=0 and y+1<n and graph[y+1][x]!=1 and graph[y+1][x]!=-1 and visited[y+1][x]==False:
            check=1
            queue.append((y+1,x))
            visited[y+1][x]=True
            if graph[y+1][x]==0 or graph[y+1][x]>graph[y][x]+1:
                graph[y+1][x]=graph[y][x]+1
        if x < m and x >=0 and y-1>=0 and y-1<n and graph[y-1][x]!=1 and graph[y-1][x]!=-1 and visited[y-1][x]==False:
            check=1
            queue.append((y-1,x))
            visited[y-1][x]=True
            if graph[y-1][x]==0 or graph[y-1][x]>graph[y][x]+1:
                graph[y-1][x]=graph[y][x]+1






        # for i in range(4):
        #     nx=x+dx[i]
        #     ny=y+dy[i]
        #     if nx<0 or nx>=m or ny<0 or ny>=n:
        #         continue
        #     if graph[ny][nx]==1:
        #         continue
        #     if graph[ny][nx]==-1:
        #         continue
        #     if visited[ny][nx]:
        #         continue
        #     if graph[ny][nx]>1 or graph[ny][nx]==0:
        #         check=1
        #         queue.append((ny,nx))
        #         visited[ny][nx]=True
        #         if graph[ny][nx]==0 or graph[ny][nx]>graph[y][x]+1:
        #             graph[ny][nx]=graph[y][x]+1

for i in range(len(start_l)):
    y,x=start_l[i]
    visited=[[False]*m for i in range(n)]
    
    bfs(y,x)
    

flag=0
for i in range(n):
    if 0 in graph[i]:
        flag=1

list_max=-99
total_max=-99
if check==1:
    print(0)
else:
    if flag==1:
        print(-1)
    else:
        for i in range(n):
            list_max=max(graph[i])
            if list_max>=total_max:
                total_max=list_max  
        print(total_max-1)            

