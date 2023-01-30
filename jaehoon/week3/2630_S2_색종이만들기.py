
def solve(board,size,y,x):
    global w,b
    
    flag=0
    std = board[y][x]
    for i in range(y,y+size):
        for j in range(x,x+size):
            if std != board[i][j]:
                flag=1
                break
        
        if flag==1:
            break
                

    if flag==1: # 재귀
        size = size//2
        solve(board,size,y,x)
        solve(board,size,y,x+size)
        solve(board,size,y+size,x)
        solve(board,size,y+size,x+size)
    else:
        if std == 0:
            w+=1
        elif std == 1:
            b+=1
        return      


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int,input().split())) for i in range(n)]
    w,b = 0,0
    solve(board,n,0,0)
    print(w)
    print(b)