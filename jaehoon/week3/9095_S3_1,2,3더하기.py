def solve(path):
    global cnt
    if sum(path) == n:
        cnt+=1
        return
    elif sum(path) > n:
        return

    for i in range(1,4):
        path.append(i)
        solve(path)
        path.pop()
    return
    
if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n = int(input())
        path, cnt = [], 0
        solve(path)
        print(cnt)