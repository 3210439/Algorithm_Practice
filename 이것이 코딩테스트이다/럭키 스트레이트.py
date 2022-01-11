
# 럭키 스트레이트
# p.321 나의 풀이
n = input()

mid = (len(n) // 2)

left = 0
right = 0

for i in range(mid):
    left += int(n[i])

for i in range(mid, len(n)):
    right += int(n[i])
    
if left == right:
    print('LUCKY')
else:
    print('READY')


  