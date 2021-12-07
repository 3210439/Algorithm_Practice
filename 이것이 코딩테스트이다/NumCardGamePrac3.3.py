n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for i in range(0,m):
  for k in range(0,n):
    arr[i][k] = int(input())
print(arr)
