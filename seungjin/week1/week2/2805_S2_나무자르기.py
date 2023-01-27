def binary_search(array,start,end,target):
    result=0
    while start<=end:
        total=0
        mid=(start+end)//2
        for i in array:
            if mid<i:
                total+=i-mid
        if total==m:
            return mid
        if total < m:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return result

if __name__ =="__main__":
    n,m=map(int,input().split())
    trees=list(map(int,input().split()))
    print(binary_search(trees,0,max(trees),m))