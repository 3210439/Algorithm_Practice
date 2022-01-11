#https://www.acmicpc.net/problem/17269

N, M = map(int, input().split())
A, B = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ''
min_len = min(N, M)
for i in range(min_len):
    AB += A[i] + B[i]

# [최대값보다 큰 인덱스:] 로 진행될 때 빈 문자열을 자동으로 반환하게 된다.
AB += A[min_len:] + B[min_len:]

lst = [alp[ord(i)-ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0]%10*10 + lst[1] % 10))