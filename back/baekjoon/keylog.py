testCase = int(input())
print('testCase: {0}'.format(testCase))
keylogs, solved = list(), list()
for _ in range(testCase):
    keylogs.append(input())

for keylog in keylogs:
    stack1,s_str = list(),list()
    temp =''
    cursor = 0
    
    for ch in range(len(keylog)):
        stack1.append(keylog[ch])
    l = len(stack1)
    for i in range(l):
        if stack1[i] == '<':
            if cursor > 0:
                cursor -=1
            continue
        elif stack1[i] == '>':
            if len(s_str) > cursor:
                cursor +=1
            continue
        elif stack1[i] == '-' :
            if cursor > 0:
                cursor -=1
                del s_str[cursor]
            continue
        else:
            s_str.insert(cursor,stack1[i])
            cursor +=1
    solved.append(s_str)
            
            

for sol in solved:
    print("".join(sol))