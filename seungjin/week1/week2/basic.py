
def binary_search(array,target,start,end):
    if start>end:
        return None

    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)


if __name__ == "__main__":
    n,target=map(int,input().split())
    numbers=list(map(int,input().split())) 
    result=binary_search(numbers,target,0,n-1)
    if result==None:
        print(-1)
    else:
        print(result+1)





