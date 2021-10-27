#https://programmers.co.kr/learn/courses/30/lessons/64061?language=python
# 인형은 1~5의 종류가 있으며0은 없는 칸이다. 

def solution(board, moves):
  answer = 0
  # basket에 -10을 넣어준 이유는 -1인덱스 접근시 out of list 에러를 방지하기 위해서이다.
  basket =[-10]
  for move in moves:
    for i in range(len(board[0])):
      print('crane: '+str(board[i][move-1]), end=' ')
      print('basket: '+str(basket),end=' ')
      print('move: '+str(+move),end=' ')
      print('answer: '+str(answer))
      if board[i][move-1] != 0:
        if basket[-1] != board[i][move-1]:
          basket.append(board[i][move-1])
          board[i][move-1] = 0
          break
        else:
          board[i][move-1] = 0
          basket.pop()
          answer+=2
          break
  return answer
  

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
