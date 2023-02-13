
def solve(y,x,cnt):
    global mincnt

    if y>=10:
        mincnt = min(mincnt,cnt)
        return
    
    if x>=10:
        solve(y+1,0,cnt)
        return

    if board[y][x] == 1:
        for k in range(5):
            if types[k] == 5:
                continue
            if y+k>=10 or x+k>=10:
                continue
            
            flag=0

            for i in range(y,y+k+1):
                for j in range(x,x+k+1):
                    if board[i][j] == 0:
                        flag=1
                        break
                if flag:
                    break


            if flag==0:
                for i in range(y,y+k+1):
                    for j in range(x,x+k+1):
                        board[i][j] = 0

                types[k]+=1
                solve(y,x+k+1,cnt+1)
                types[k]-=1

                for i in range(y,y+k+1):
                    for j in range(x,x+k+1):
                        board[i][j] = 1
    else:
        solve(y,x+1,cnt)

    return


if __name__ == "__main__":
    board = [list(map(int,input().split())) for i in range(10)]
    types = [0,0,0,0,0]
    mincnt = 26
    solve(0,0,0)
    if mincnt == 26:
        print(-1)
    else:
        print(mincnt)