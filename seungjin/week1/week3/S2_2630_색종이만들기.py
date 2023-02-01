def divide(row,col,n):
    global w,b
    color=array[row][col]
    for i in range(row,row+n):
        for j in range(col,col+n):
            if array[i][j]!=color:
                divide(row,col,n//2)
                divide(row,col+n//2,n//2)
                divide(row+n//2,col,n//2)
                divide(row+n//2,col+n//2,n//2)
                return
    if color==0:
        w+=1
    else:
        b+=1
    return



if __name__=="__main__":
    n=int(input())
    array=[]
    for i in range(n):
        array.append(list(map(int, input().split())))
    w,b=0,0
    divide(0,0,n)
    print(w)
    print(b)