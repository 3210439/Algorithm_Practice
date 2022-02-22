# 1번 풀이
n = int(input())
data = []

for i in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    data.append([a, b, c, name])

data = sorted(data, key = lambda x : (-x[0], x[1], -x[2], x[3]))

for i in range(n):
    print(data[i][3])




# 2번 풀이
n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())


students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])