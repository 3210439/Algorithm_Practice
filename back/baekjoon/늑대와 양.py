# https://www.acmicpc.net/problem/16956
r, c = map(int, input().split())
m = [list(input()) for i in range(r)]
result = False

dx, dy = [-1,1,0,0], [0,0,1,-1]

for i in range(r):
    for j in range(c):
        if m[i][j] == 'W':
            for k in range(4):
                xn = dx[k] + i
                yn = dy[k] + j
                if 0 <= xn and xn < r and 0 <= yn and yn < c:
                    if m[xn][yn] == 'S':
                        result = True

if result == True:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if m[i][j] == '.':
                m[i][j] = 'D'

    for i in m:
        print(''.join(i))
