def divide(y,x,n):
    global now
    
    if n!=2:
        divide(y,x,n//2)
        divide(y,x+n//2, n//2)
        divide(y+n//2,x,n//2)
        divide(y+n//2,x+n//2,n//2)
        return
    array[y][x]=now
    now+=1
    array[y][x+1]=now
    now+=1
    array[y+1][x]=now
    now+=1
    array[y+1][x+1]=now
    now+=1
    if y+1==n-1 and x+1==n-1:
        return



if __name__=="__main__":
    now=0
    n,r,c=map(int,input().split())
    array=[[0]*(2**n) for i in range(2**n)]
    divide(0,0,2**n)
    print(array[r][c])