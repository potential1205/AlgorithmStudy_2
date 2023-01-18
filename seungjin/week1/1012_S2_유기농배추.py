from collections import deque

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

T=int(input())
answer=[]
for i in range(T):
    result=0
    m,n,k=map(int,input().split())
    graph=[[0]*m for l in range(n)]
    for j in range(k):
        b,a=map(int,input().split())
        graph[a][b]=1
    for j in range(n):
        for k in range(m):
            if dfs(j,k)==True:
                result+=1
    answer.append(result)
for i in answer:
    print(i)