from collections import deque

def bfs(network,start):
    queue = deque([start])
    visit = [False] * (n+1)
    cnt = 0

    while queue:
        host = queue.popleft()
        visit[host] = True
        for com in network[host]:
            if visit[com] == False:
                cnt+=1
                queue.append(com)
                visit[com] = True
                
    return cnt

def dfs(network,visit,com):
    global cnt
    visit[com] = True
    cnt+=1
    for temp in network[com]:
        if visit[temp] == False:
            dfs(network,visit,temp)

    return

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    network = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        network[a].append(b)
        network[b].append(a)

    # bfs
    #print(bfs(network,1))

    #dfs
    visit = [False] * (n+1)
    cnt=0
    dfs(network,visit,1)
    print(cnt-1)



