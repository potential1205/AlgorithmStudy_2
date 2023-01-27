from collections import deque
def bfs(graph,i,j,visited):
    save_index=[]
    queue=deque()
    queue.append((i,j))
    visited[i][j]=True
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if nx<0 or nx >=N or ny<0 or ny>=N:
                continue
            if not visited[ny][nx]:
                if L <= abs(graph[y][x]-graph[ny][nx]) <=R:
                    queue.append((ny,nx))
                    visited[ny][nx]=True
                    save_index.append((ny,nx))


if __name__ =="__main__":
    N,L,R=map(int,input().split())
    graph=[]
    for i in range(N):
        graph.append(list(map(int,input().split())))
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    result=0
    result_flag=0
    while True:
        visited=[[False]*(N) for i in range(N)]
        result_flag=0
        for i in range(N):
            for j in range(N):
                if bfs(graph,i,j,visited)==1:
                    
                    result_flag=1
        
        if result_flag==0:
            break
        result+=1
            
    print(result)