
def solve(info):
    pop = 0
    for i in range(n):
        k = info[i][1]
        pop = pop + k

    mid = pop//2

    if (pop%2) != 0: 
        mid = mid + 1
    
    pop = 0
    for q,w in info:
        pop += w 
        if pop >= mid:
            ans = q
            break
    
    return ans


if __name__ == "__main__":
    
    n = int(input())
    info = [list(map(int,input().split())) for _ in range(n)]
    
    info.sort(key=lambda x : (x[0]))
    print(solve(info))
    
    


        

