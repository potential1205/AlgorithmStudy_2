import heapq
import sys

def solve(lst):
    heap = []
    for val in lst:
        heapq.heappush(heap,val)
    
    result = 0
    for i in range(n-1):
        val1 = heapq.heappop(heap)
        val2 = heapq.heappop(heap)
        result = result + val1 + val2
        heapq.heappush(heap,val1+val2)
    print(result)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n = int(input())
        lst = list(map(int,sys.stdin.readline().split()))
        lst.sort()
        solve(lst)
        