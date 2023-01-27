def solution(trees,m):
    start,end = 0,trees[-1]
    while start<=end:
        mid = (start+end) // 2
        cum = 0
        for tree in trees:
            if tree-mid < 0:
                continue
            cum = cum + (tree-mid)
        
        if cum == m:
            return mid
        elif cum < m:
            end = mid-1
        elif cum > m:
            start = mid+1
    
    return (start+end)//2 # 왜 mid를 return하면 오답일까


if __name__ == "__main__":
    n,m = map(int,input().split())
    trees = list(map(int,input().split()))
    trees.sort()
    print(solution(trees,m))