import sys

if __name__ == "__main__":
    n = int(input())

    min_dp = [0,0,0]
    min_tmp = [0,0,0]

    for i in range(n):
        a,b,c = map(int,sys.stdin.readline().split())
        min_tmp[0] = a + min(min_dp[1],min_dp[2])
        min_tmp[1] = b + min(min_dp[0],min_dp[2])
        min_tmp[2] = c + min(min_dp[0],min_dp[1])

        min_dp[0] = min_tmp[0]
        min_dp[1] = min_tmp[1]
        min_dp[2] = min_tmp[2]

    print(min(min_tmp))