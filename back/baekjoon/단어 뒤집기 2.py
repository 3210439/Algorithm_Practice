# 17413 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
S = input()
ans, tmp, ck, last = "", "", False, len(S)-1

for w in S:
    if w == " ":
        if not ck:
            ans += tmp[::-1] + " "
            tmp = ""
        else:
            ans += " "
    elif w == "<":
        ans += tmp[::-1] + "<"
        tmp = ""
        ck = True
    elif w == ">":
        ck = False
        ans += ">"
    else:
        if ck: ans += w
        else : tmp += w
if tmp != "":
    ans += tmp[::-1]

print(ans)