
if __name__ == "__main__":
    n,k = map(int,input().split())
    cache = [0] * (k+1)

    for _ in range(n):
        w, v = map(int,input().split())
        for j in range(k, w-1, -1):
            cache[j] = max(cache[j], cache[j-w] + v)
    print(cache[-1])