import operator
def solution(N, stages):
    answer = {}
    leng = len(stages)
    print(leng)
    
    cnt = [0] * (500)
    
    for stage in stages:
        for i in range(0,stage):
            cnt[i] +=1
    
    for i in range(N):
        if cnt[i] == 0:
            answer[i+1] = 0
        else:
            val = cnt[i] - cnt[i+1]
            answer[i+1] = val/cnt[i]
        
    d1 = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)
    a=[]
    for i in range(N):
        a.append(d1[i][0])


    return a




import operator
def solution(N, stages):
    answer = []
    user_len = len(stages)
    info = [0] * user_len
    
    for i in range(N):
        solve_num = 0
        try_num = 0
        for j in range(user_len):
            if (i+1) <= stages[j]:
                solve_num +=1
            if (i+1) < stages[j]:
                try_num +=1
                
        if (solve_num) == 0:
            answer.append(0)
        else:
            answer.append([i+1,(solve_num-try_num)/solve_num])
    
    
    answer.sort(key = lambda x :(-x[1], x[0]))
    a = []
    for i in range(len(answer)):
        a.append(answer[i][0])
    
    return a