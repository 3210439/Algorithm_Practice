#https://www.acmicpc.net/problem/16165

N, M = map(int, input().split())
groupDict, mem_team = {}, {}

for _ in range(N):
    groupName = input()
    groupDict[groupName] = list()
    groupNum = int(input())
    for _ in range(groupNum):
        girlName = input()
        groupDict[groupName].append(girlName)
        mem_team[girlName] = groupName

for i in range(M):
    problem = input()
    kinds = int(input())

    # question for name
    if kinds == 1:
        print(mem_team[problem])
    elif kinds == 0:
        for girl in sorted(groupDict[problem]):
            print(girl)
