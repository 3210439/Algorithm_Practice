#https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >=2:   
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        temp = min1 + min2*2
        heapq.heappush(scoville,temp)
        answer +=1
        if K <= scoville[0]:
            return answer      
    return -1