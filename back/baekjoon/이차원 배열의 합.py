# 구현 풀이 방법
n, m = map(int, input().split())
lst = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, m+1):
        lst[i][j] = tmp[j-1]

k = int(input())
k_lst = [list(map(int, input().split())) for _ in range(k)]
result = []

for _ in range(k):
    a,b,x,y = k_lst[i][0], k_lst[i][1], k_lst[i][2], k_lst[i][3]
    sum = 0
    for i in range(a,x+1):
        for j in range(b, y+1):
            sum += lst[i][j]
    result.append(sum)

for i in range(len(result)):
    print(result[i])

# DP로 푸는 방법
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# DP[i][j] = 1, 1부터 (i, j)까지의 부분합
DP = [[0 for i in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]
        
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])
    