
def binary_search(seq,val):

    start, end = 0, len(seq)

    while start+1<end:
        mid = (start+end)//2
        if val > seq[mid]:
            start = mid
        else:
            end = mid
        
    return end


def solve(n,lst):

    seq = [-float('inf')]
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        if lst[i] > seq[-1]:
            dp[i] = len(seq)-1
            seq.append(lst[i])
        else:
            dp[i] = binary_search(seq,lst[i])
            seq[dp[i]] = lst[i]
            
    print(len(seq)-1)

    max_idx,ans = max(dp)+1,[]
    for i in range(n,0,-1):
        if dp[i] == max_idx-1:
            ans.append(lst[i])
            max_idx = dp[i]
    print(*ans[::-1])

    return

if __name__ == "__main__":
    n = int(input())
    lst = [0] + list(map(int,input().split()))
    solve(n,lst)