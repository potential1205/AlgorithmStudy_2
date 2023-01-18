from collections import deque

def dfs(graph,v,visit):
    print(v,end=" ")
    visit[v] = True
    for node in graph[v]:
        if visit[node] == False:
            dfs(graph,node,visit)
    return

def bfs(graph,v,n):
    queue = deque([v])
    visit = [False] * (n+1)

    while queue:
        node = queue.popleft()
        visit[node] = True
        print(node,end=' ')
        for temp in graph[node]:
            if visit[temp] == True:
                continue
            queue.append(temp)
            visit[temp] = True
    return


if __name__ == "__main__":
    n,m,v = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(n+1):
        graph[i].sort()

    visit = [False] * (n+1)
    dfs(graph,v,visit)
    print("")
    bfs(graph,v,n)