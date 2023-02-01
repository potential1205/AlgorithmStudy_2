def solution(survey, choices):
    answer,info = [],dict()
    type = ["R","T","C","F","J","M","A","N"]
    for i in range(len(type)):
        info[type[i]] = 0
    
    for i in range(len(survey)):
        if choices[i]<=3:
            info[survey[i][0]]+= 4-choices[i]
        elif choices[i]>=5:
            info[survey[i][1]]+= choices[i]-4
            
    for i in range(0,len(type),2):
        l,r = info[type[i]], info[type[i+1]]
        answer.append(type[i] if l>=r else type[i+1])

    return "".join(answer)