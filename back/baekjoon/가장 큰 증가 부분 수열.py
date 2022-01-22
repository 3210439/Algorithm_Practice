import copy

n, k = int(input()), list(map(int, input().split()))
dp = copy.deepcopy(k)

for i in range(1,n):
    for j in range(i):
        if k[i] > k[j] and dp[i] < dp[j] + k[i]:
            dp[i] = dp[j] + k[i]
print(max(dp))