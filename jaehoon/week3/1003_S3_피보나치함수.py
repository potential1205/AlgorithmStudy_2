
def solve(n):
    if n==0:
        print("1 0")
    else:   
        zero, one = 0,1
        for i in range(n-1):
            zero, one = one, one+zero
        print(zero,one)
    return

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n = int(input())
        solve(n)
        
