# n 배열과 좌표 문자열이 주얼때 여행자의 위치는 ??

def upDownLeftRight_mine(n, coordinates):
    arr = [[0]*(n+1) for _ in range(n+1)]
    coor = list(coordinates.split(' '))
    x,y = 1, 1
    for cor in coor:
        if cor == 'R':
            if x < n:
                x += 1
        elif cor == 'U':
            if y > 1 :
                y -=1
        elif cor == 'L' :
            if x > 1 :
                x -=1
        elif cor == 'D' :
            if y < n :
                y += 1
    print(str(y) +' ' + str(x))

def upDownLeftRight_sol(n, plans):
    x, y = 1, 1

    # L, R, U, D에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
    print(x, y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    upDownLeftRight_mine(5, 'R R R U D D')
    upDownLeftRight_sol(5, 'R R R U D D')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
