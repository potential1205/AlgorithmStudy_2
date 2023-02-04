from collections import deque
if __name__=="__main__":
    n=int(input())
    k=int(input())
    apple=[]
    snakehead=[1,1]
    cnt=0
    dx=[-1,0,1,0]
    dy=[0,-1,0,1] #왼쪽 부터 시계방향으로 0,1,2,3
    snake=deque()
    snake.append([1,1])
    now_direction=2
    move=[]
    for i in range(k):
        ay,ax=map(int,input().split())
        apple.append([ay,ax])
    l=int(input())
    for i in range(l):
        x,c=map(str,input().split())
        x=int(x)
        move.append((x,c))
    flag=0
    now=0
    move.append([102,"F"])
    for x,c in move:
        if flag==1:
            break
        for j in range(x-now):
            snake_head=snake[-1]
            #print(f"snake_head : {snake_head}")
            ny,nx=snake_head[0]+dy[now_direction],snake_head[1]+dx[now_direction]
            #print(f"y,x:{ny,nx}")
            cnt+=1
            if nx<=0 or nx>n or ny<=0 or ny>n:
                flag=1
                #print("1out")
                break
            if [ny,nx] in snake:
                flag=1
                #print("2out")
                break
            snake.append([ny,nx])
            if [ny,nx] not in apple:
                snake.popleft()
            else:
                apple.remove([ny,nx])
        
            #print(f"cnt:{cnt}")
            #print(f"snake: {snake}")
        now=x
        if c=="D":
            now_direction+=1
        else:
            now_direction-=1
        now_direction=now_direction%4
        #print(f"now_direction: {now_direction}")
        #print(f"snake: {snake}")
        
    print(cnt)




        