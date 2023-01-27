from collections import deque

def solution(n,k):
    queue = deque([[n,0]])
    visit = [False] * 100001

    while queue:
        x,level = queue.popleft()
        visit[x] = True
        if x == k:
            return level

        if 0<= x+1 <= 100000 and visit[x+1] == False:
            queue.append([x+1,level+1])
            visit[x+1] = True
        
        if 0<= x-1 <= 100000 and visit[x-1] == False:
            queue.append([x-1,level+1])
            visit[x-1] = True

        if 0<= 2*x <= 100000 and visit[2*x] == False:
            queue.append([2*x,level+1])
            visit[2*x] = True 


if __name__ == "__main__":
    n,k = map(int,input().split())
    print(solution(n,k))