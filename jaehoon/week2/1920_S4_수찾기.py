
def solution(lst_n,val):
    start,end = 0,len(lst_n)-1

    while start <= end:
        mid = (start+end)//2

        if lst_n[mid] == val:
            return 1
        elif lst_n[mid] > val:
            end = mid-1
        elif lst_n[mid] < val:
            start = mid+1
    
    return 0


if __name__ == "__main__":
    n = int(input())
    lst_n = list(map(int,input().split()))
    lst_n.sort()

    m = int(input())
    lst_m = list(map(int,input().split()))

    for val in lst_m:
        print(solution(lst_n,val))
