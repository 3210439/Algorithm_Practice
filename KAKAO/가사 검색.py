# 나의 풀이(시간 초과)
def solution(words, queries):
    answer = [0 for _ in range(len(queries))]
    for i in range(len(queries)):
        for j in range(len(words)):
            if compare(queries[i], words[j]):
                answer[i] += 1
    return answer

def compare(query, word):
    if len(query) != len(word):
        return False
    for i in range(len(query)):
        if query[i] == '?':
            continue
        if query[i] != word[i]:
            return False
    return True

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))


# 답안 예시
