lst = list(map(int, list(input())))
div = len(lst) // 2

left = sum(lst[0:div])
right = sum(lst[div:])

if left == right:
    print('LUCKY')
else:
    print('READY')