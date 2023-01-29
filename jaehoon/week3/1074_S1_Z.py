
def solve(y,x,size):
    if size==2:
        if y==r and x==c:
            info.append(1)
        elif y==r and x+1==c:
            info.append(2)
        elif y+1==r and x==c:
            info.append(3)
        elif y+1==r and x+1==c:
            info.append(4)
        return

    size = size//2
    if x <= c < x+size and y <= r < y+size:
        info.append(1)
        solve(y,x,size)
    
    elif x <= c < x+2*size and y <= r < y+size:
        info.append(2)
        solve(y,x+size,size)
        
    elif x <= c < x+size and y <= r < y+2*size:
        info.append(3)
        solve(y+size,x,size)
        
    elif x <= c < x+2*size and y <= r < y+2*size:
        info.append(4)
        solve(y+size,x+size,size)

if __name__ == "__main__":
    n,r,c = map(int,input().split())
    info, size = [], 2**n
    solve(0,0,size)

    result, val = 0 , size*size
    for i in range(n):
        val //= 4
        result += ((info[i]-1)*val)
    print(result)