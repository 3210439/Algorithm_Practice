n, a = int(input()), sorted(list(map(int, input().split())))
ans = 0

for v in a:
    if ans+1 >= v:
        ans += v
    else:
        break;
print(ans+1)