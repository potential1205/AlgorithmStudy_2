def solution(survey, choices):
    mbti={'R':0, 'T':0, 'C':0 , 'F':0 , 'J':0 , 'M':0 , 'A':0 , 'N':0}
    for i in range(len(survey)):
        if choices[i]>=5:
            mbti[survey[i][1]]+=(choices[i]-4)
        elif choices[i]<5:
            mbti[survey[i][0]]+=(4-choices[i])
    answer=[]
    result=[]
#     if mbti['R']>=mbti['T']:
#         answer.append('R')
#     else:
#         answer.append('T')
        
#     if mbti['C']>=mbti['F']:
#         answer.append('C')
#     else:
#         answer.append('F')
        
#     if mbti['J']>=mbti['M']:
#         answer.append('J')
#     else:
#         answer.append('M')
        
#     if mbti['A']>=mbti['N']:
#         answer.append('A')
#     else:
#         answer.append('N')
#     result=''.join(answer)

    print(mbti)
    answer=[[k,v] for k,v in mbti.items()]
    print(answer)
    for i in range(0,8,2):
        print(i)
        if answer[i][1]>=answer[i+1][1]:
            result.append(answer[i][0])
        else:
            result.append(answer[i+1][0])
    
    ans=''.join(result)
    print(ans)
    return ans



















# answer=''
#     type={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0,}
#     for i in range(len(survey)):
#         if choices[i]==4:
#             continue
#         elif choices[i]>4:
#             type[survey[i][1]]+=choices[i]-4
#         elif choices[i]<4:
#             type[survey[i][0]]+=4-choices[i]
#     print(type.items())
#     if type['R']<type['T']:
#         answer+='T'
#     else:
#         answer+='R'
        
        
#     if type['C']<type['F']:
#         answer+='F'
#     else:
#         answer+='C'
        
        
#     if type['J']<type['M']:
#         answer+='M'
#     else:
#         answer+='J'
        
        
#     if type['A']<type['N']:
#         answer+='N'
#     else:
#         answer+='A'