#이코테 312.p 나의 답안
#각 자리가 숫자로만 이루어진 문자열S 가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩
#모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+'연산자를 넣어 결과적으로 만들어 질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요 
if __name__ == '__main__':
    s = input()
    arr = []
    for i in range(len(s)):
        arr.append(int(s[i]))

    result = arr[0]
    for i in range(1, len(arr)):
        multiply = result * arr[i]
        plus = result + arr[i]
        result = max(multiply, plus)
    print(result)
