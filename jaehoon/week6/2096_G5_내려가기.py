import sys

if __name__ == "__main__":
    n = int(input())

    max_tmp = [0,0,0]
    min_tmp = [0,0,0]

    max_dp = [0,0,0]
    min_dp = [0,0,0]
    
    for i in range(n):
        a,b,c = map(int,sys.stdin.readline().split())
        for j in range(3):
            if j == 0:
                max_tmp[j] = a + max(max_dp[j],max_dp[j+1])
                min_tmp[j] = a + min(min_dp[j],min_dp[j+1])
            
            elif j == 1:
                max_tmp[j] = b + max(max_dp[j-1],max_dp[j],max_dp[j+1])
                min_tmp[j] = b + min(min_dp[j-1],min_dp[j],min_dp[j+1])
            
            else:
                max_tmp[j] = c + max(max_dp[j-1],max_dp[j])
                min_tmp[j] = c + min(min_dp[j-1],min_dp[j])
        
        for j in range(3):
            max_dp[j] = max_tmp[j]
            min_dp[j] = min_tmp[j]
    

    print(max(max_tmp),min(min_tmp))

