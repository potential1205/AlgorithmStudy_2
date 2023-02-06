import sys
input = sys.stdin.readline

def solve(info):
    mid = round(sum(col for row, col in info)/2)

    total = 0
    for x,pop in info:
        total += pop
        if total >= mid:
            ans = x
            break
    
    return ans

if __name__ == "__main__":
    n = int(input())
    info = [list(map(int,input().split())) for _ in range(n)]
    info.sort(key=lambda x : (x[0]))
    print(solve(info))