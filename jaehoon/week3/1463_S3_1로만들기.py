from collections import deque
MAX = 10**6

def solve(n):
    queue = deque([[n,0]])
    visit = [False] * (MAX+1)

    while queue:
        val,level = queue.popleft()
        visit[val] = True

        if val == 1:
            return level

        if val % 3 == 0 and 1<= val//3 < MAX and visit[val//3] == False: 
            queue.append([val//3,level+1])
            visit[val//3] = True
        if val % 2 == 0 and 1<= val//2 < MAX and visit[val//2] == False: 
            queue.append([val//2,level+1])
            visit[val//2] = True
        if  1<= val-1 < MAX and visit[val-1] == False:  
            queue.append([val-1,level+1])
            visit[val-1] = True
      
    return level

if __name__ == "__main__":
    n = int(input())
    print(solve(n))