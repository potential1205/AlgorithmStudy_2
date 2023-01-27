from collections import deque
n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# visited=[False]*(n+1)

# def bfs(graph,start,visited):
#     queue=deque([start])
#     visited[start]=True
#     result=0
#     while queue:
#         v=queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True
#                 result+=1
    
#     return result
# print(bfs(graph,1,visited))

# print(graph)
visited=[False]*(n+1)

global res
res=0
def dfs(graph,v,visited):
    visited[v]=True
    global res
    res+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return res-1
print(dfs(graph,1,visited))