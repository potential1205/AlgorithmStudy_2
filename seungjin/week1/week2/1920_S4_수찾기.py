def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        if array[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return 0


if __name__=="__main__":
    n=int(input())
    A=list(map(int,input().split()))
    A.sort()
    m=int(input())
    B=list(map(int,input().split()))
    for i in B:
        result=binary_search(A,i,0,n-1)
        print(result)


