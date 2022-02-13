n, m = map(int, input().split())
chickens, home, score, city_score = [], [], [], []


def cal(chicken, home):
    sum = 0
    for i in range(len(home)):
        sum += abs(chicken[0] - home[i][0]) + abs(chicken[1] - home[i][1])
    return sum


def find_nearest(home_, chickens_):
    temp = 555
    for chi in chickens_:
        result = abs(home_[0] - chi[0]) + abs(home_[1] - chi[1])
        temp = min(temp, result)
    return temp


for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    for j in range(1, n + 1):
        if lst[j - 1] == 1:
            home.append((i, j))
        elif lst[j - 1] == 2:
            chickens.append((i, j))

for i in range(len(chickens)):
    sum = cal(chickens[i], home)
    score.append((chickens[i], sum))

score.sort(key = lambda x:-x[1])

while len(score) > m:
    temp = score.pop(0)
    chickens.remove(temp[0])

for i in range(len(home)):
    temp_sum = find_nearest(home[i], chickens)
    city_score.append((home[i], temp_sum))
print('city_score'+city_score)
print('chickens'+chickens)
answer = 0
for i in range(len(city_score)):
    answer += city_score[i][1]

print(answer)




