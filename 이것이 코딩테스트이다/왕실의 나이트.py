# 해당 문제는 간단한 구현 문제지만 dfs나 bfs 문제를 풀때 많은 도움을 줄 수 있을 것으로 보인다.

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의 
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result = 0
for step in steps:
  next_row = row + step[1]
  next_column = column + step[0]

  if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
    result += 1
print(result)