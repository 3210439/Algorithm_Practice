lst = list(input())
strs, nums = '',0

for ch in lst:
    if ord('A') <= ord(ch):
        strs += ch
    else:
        nums += int(ch)

answer = strs + str(nums)
print(answer)


