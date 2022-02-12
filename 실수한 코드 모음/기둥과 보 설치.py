# 실패 사유 
# 시뮬레이션 문제를 너무 단순하게 생각학 풀었다.

def solution(n, build_frame):
    lst = [[3 for _ in range(n+1)] for _ in range(n+1)]
    answer = []
    for i in range(len(build_frame)):
        # 기둥일 경우
        if build_frame[i][2] == 0 and build_frame[i][3] == 1:
            # 기둥은 바닥 위에 있다.
            # 보의 한쪽 끝 위에 있다.x-1, y-1 == 1
            # 또다른 기둥 위에 있다 x, y-1 == 0
            x, y = build_frame[i][0], build_frame[i][1]
            if build_frame[i][1] == 0 or lst[y][x-1] == 1 or lst[y-1][x] == 0:
                lst[y][x] = 0
        # 기둥 삭제
        # x, y + 1 좌표에 기둥 혹은 보가 있으면 안된다.
        elif build_frame[i][2] == 0 and build_frame[i][3] == 0:
            if lst[y+1][x] == 3:
                lst[y][x] = 3

        elif build_frame[i][2] == 1 and build_frame[i][3] == 1:
            # 보는 한쪽 끝부분이 기둥
            # 양쪽 끝부분이 다른 보와 동시에 연결
            if lst[y-1][x] == 0 or (lst[y][x+1] == 1 and lst[y][x-1] == 1):
                lst[y][x] = 1

        # 보 삭제
        # x, y + 1 좌표에 기둥 혹은 보가 있으면 안된다.
        elif build_frame[i][2] == 1 and build_frame[i][3] == 0:
            if lst[y][x+1] != 0:
                lst[y][x] = 3

    for i in range(n+1):
         for j in range(n+1):
            if lst[j][i] != 3:
                answer.append([i,j,lst[j][i]])

    return answer

