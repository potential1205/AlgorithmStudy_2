def up_down_fibo(m):
    global num_0
    global num_1
    if m==0:
        dp_cnt[0][0]=1
        return 0
    if m==1:
        dp_cnt[1][1]=1
        return 1
    if dp[m]!=-1:
        return dp[m]
    dp[m]=up_down_fibo(m-1)+up_down_fibo(m-2)
    dp_cnt[m][0]=dp_cnt[m-1][0]+dp_cnt[m-2][0]
    dp_cnt[m][1]=dp_cnt[m-1][1]+dp_cnt[m-2][1]
    return dp[m]
if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        m=int(input())
        dp=[-1]*41
        dp_cnt=[[0,0] for i in range(41)]
        dp_cnt[0]
        num_1=0
        num_0=0
        up_down_fibo(m)
        print(dp_cnt[m][0],dp_cnt[m][1])
