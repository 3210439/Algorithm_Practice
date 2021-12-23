# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 해당 문제는 이것이 코딩 테스트이다. 의 DP 편 개미 전사 문제입니다.
# 해당 문제를 혼자 해결해보려 했지만 20분간 정도의 고민후 아이디어가 
# 떠오르지 않아 해설과 답안을 참조했습니다.
# DP 문제는 답안을 봐도 처음에 이해하기 어려우니 자주 학습이 필요할 것 같습니다.
# 일직선으로 존재하는 메뚜기의 식량창고가 존재합니다.
# 메뚜기 정찰병에게 들키지 않고 약탈하기 위해서는 최소 한칸 이상 떨어진
# 식량 창고를 약탈해야 합니다.
# 점화식은 다음과 같습니다.
# a(i) = max(a(i-1), a(i-2) +k)
# 점화식은 간단하지만 점화식을 구하는 것은 많은 경험이 필요할 거 같습니다. 
if __name__ == '__main__':
    # 정수 N을 입력받기
    n = int(input())
    # 모든 식량 정보 입력받기
    array = list(map(int, input().split()))

    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 100

    # 다이나믹 프로그래밍 (Dynamic Programming) 진행(보텀업)
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    # 계산된 결과 출력
    print(d[n - 1])
