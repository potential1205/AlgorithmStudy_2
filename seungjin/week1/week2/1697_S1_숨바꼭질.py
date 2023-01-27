from collections import deque
def bfs(array,n,m):
    queue=deque([n])
    while queue:
        v=queue.popleft()
        if v==m:
            return
        for i in (v+1, v-1, v*2):
            if i<0:
                continue
            if i>=100001:
                continue  
            if array[i]==0:
                array[i]=array[v]+1
                queue.append(i)
                 
if __name__=="__main__":
    n,m=map(int,input().split())
    array=[0]*100001
    bfs(array,n,m)
    print(array[m])