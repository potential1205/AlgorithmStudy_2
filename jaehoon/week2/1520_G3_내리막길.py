dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solve(sy,sx):
    if sy == n-1 and sx == m-1:
        return 1

    if path_board[sy][sx] != -1:
        return path_board[sy][sx]

    cnt = 0
    for i in range(4):
        ky,kx = sy+dy[i],sx+dx[i]
        if ky<0 or kx<0 or ky>=n or kx>=m:
            continue
        if board[ky][kx]<board[sy][sx]:
            cnt = cnt + solve(ky,kx)

    path_board[sy][sx] = cnt

    return cnt


if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for i in range(n)]
    visit = [[False for j in range(m)] for i in range(n)]
    path_board = [[-1 for j in range(m)] for i in range(n)]
    print(solve(0,0))
