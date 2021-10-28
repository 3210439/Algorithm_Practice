#https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def qsort(array):
    if len(array) <= 1 : 
        return array
    pivot = array[0]
    left, right = list(), list()
    try:
        for i in range(1,len(array)):
            if pivot < array[i]:
                right.append(array[i])
            else:
                left.append(array[i])
    
    except IndexError as e:
        print('inininininin')
    return qsort(left) + [pivot] + qsort(right)

def solution(array, commands):
    answer = []
    for com in commands:
        list1 = array[com[0]-1:com[1]]
        list2 = qsort(list1)
        #print(list2)
        answer.append(list2[com[2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))