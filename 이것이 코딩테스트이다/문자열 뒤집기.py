
# 문자열 뒤집기 P.313
if __name__ == '__main__':
    s = input()
    z = 0
    o = 0

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i-1] == '0':
                z += 1
            else:
                o += 1
        if s[i] == s[i-1] and i == len(s)-1:
            if s[i] == '0':
                z += 1
            else:
                o += 1

    print(min(z,o))