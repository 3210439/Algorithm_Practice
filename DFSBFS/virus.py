# https://www.acmicpc.net/problem/2606
# 기본 bfs로 문제를 해결하였다.
# 해당 문제를 통해 bfsList 생성 방법을 다시 배웠다
n = int(input())
v = int(input())
bfsList = [[] for _ in range(n+1)]
visited = []
need_visit = []
need_visit.append(1)

for _ in range(v):
    num1, num2 = map(int, input().split())
    bfsList[num1].append(num2)
    bfsList[num2].append(num1)
    
while need_visit:
    nv = need_visit.pop()
    if nv not in visited:
        visited.append(nv)
        for n in bfsList[nv]:
            need_visit.append(n)
print(len(visited)-1)
    
  