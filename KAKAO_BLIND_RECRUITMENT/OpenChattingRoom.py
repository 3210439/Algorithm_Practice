#https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
def solution(record):
    answer = []
    NameDic = {}
    InOutList = []
    
    for element in record:
        if element.count(' ') ==2:
            InOut, UserId, Name = map(str,element.split(' '))
            NameDic[UserId] = Name
        elif element.count(' ') == 1:
            InOut, UserId = map(str,element.split(' '))
        if InOut != 'Change':
            InOutList.append((UserId,InOut))
    for temp in InOutList :
        Name = NameDic[temp[0]]
        if temp[1] == 'Enter':
            msg = Name + '님이 들어왔습니다.'
        if temp[1] == 'Leave':
            msg = Name + '님이 나갔습니다.'
        answer.append(msg)
    return answer