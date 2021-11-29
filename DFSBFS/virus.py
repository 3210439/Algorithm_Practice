# https://www.acmicpc.net/problem/2606
# 기본 bfs로 문제를 해결하였다.
# 해당 문제를 통해 bfsList 생성 방법을 다시 배웠다
#bfs 방식
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
    
#dfs 방식
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)
            
dfs(1)
print(count -1)