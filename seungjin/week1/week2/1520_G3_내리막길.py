import sys
from collections import deque
sys.setrecursionlimit(10**8)
#세로 m 가로 n


def dfs(y,x):
    if y==m-1 and x==n-1:
        return 1
    if paths[y][x]!=-1:
        return paths[y][x]
    paths[y][x]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[ny][nx]<graph[y][x]:
            paths[y][x]+=dfs(ny,nx)
    return paths[y][x]
             
if __name__ =="__main__":
    m,n=map(int,input().split())
    graph=[]
    for i in range(m):
        graph.append(list(map(int,input().split())))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    paths=[[-1]*n for i in range(m)]
    print(dfs(0,0))


