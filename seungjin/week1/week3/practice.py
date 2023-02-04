# dp=[0]*100
# def up_down_fibo(n):
#     if n==1 or n==2:
#         return 1
#     if dp[n]!=0:
#         return dp[n]
#     dp[n]=up_down_fibo(n-1)+up_down_fibo(n-2)
#     return dp[n]

# def bottom_up_fibo(n):
#     dp=[0]*100
#     dp[1]=1
#     dp[2]=1
#     for i in range(3,n+1):
#         dp[i]=dp[i-1]+dp[i-2]
#     return dp[n]
# print(up_down_fibo(4))
# print(bottom_up_fibo(4))


# def ant_warrior(): ##개미전사
#     n=int(input())
#     food=list(map(int,input().split()))
#     dp=[0]*len(food)
#     dp[0]=food[0]
#     dp[1]=food[1]
#     for i in range(2,len(food)):
#         dp[i]=max(dp[i-1],dp[i-2]+food[i])
#     print(dp[n-1])
#     return

# ant_warrior()

# def make1(): ##1만들기
#     n=int(input())
#     dp=[0]*30001
#     for i in range(2,n+1):
#         dp[i]=dp[i-1]+1
#         if i%2==0:
#             dp[i]=min(dp[i],dp[i//2]+1)
#         if i%3==0:
#             dp[i]=min(dp[i],dp[i//3]+1)
#         if i%5==0:
#             dp[i]=min(dp[i],dp[i//5]+1)
#     print(dp[n])
# make1()

def cash(): #효율적인 화폐구성
    n,m=map(int,input().split())
    money=[]
    dp=[0]*10001
    for i in range(n):
        p=int(input())
        money.append(p)
    for i in range(2,n+1):
        if i%2==0 and i%3==0:
            dp[i]=min(dp[i//2]+1,dp[i//3]+1)
        if i%2==0 and i%3!=0:
            dp[i]=dp[i//2]+1
        if i%2!=0 and i%3==0:
            dp[i]=dp[i//3]+1
        if i%2!=0 and i%3!=0:
            return -1

    return dp[n]
print(cash())
