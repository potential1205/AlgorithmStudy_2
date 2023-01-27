def solution(N, stages):
    fail=[]
    answer=[]
    for stage in range(1,N+1):
        clear=[i for i in stages if stage<=i]
        unclear=[i for i in stages if stage==i]
        if len(clear)!=0:
            fail.append(len(unclear)/len(clear))
        else:
            fail.append(0)
    
    print(fail)
    l=[]
    for t in enumerate(fail):
        l.append(t)
    l.sort(key=lambda x : x[1],reverse=True)
    for i in l:
        answer.append(i[0]+1)
    print(answer)
    
    return answer

