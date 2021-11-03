def solution(n, lost, reserve):
    answer = 0
    count = 0
    for i,lost_in in enumerate(lost):
      if lost_in in reserve:
        reserve.remove(lost_in);
        lost[i] = -99
        count +=1;
            
    for lost_in in lost:
      if lost_in-1 in reserve:
        reserve.remove(lost_in-1)
        count += 1
      elif lost_in+1 in reserve:
        reserve.remove(lost_in+1)
        count += 1
    answer = n - len(lost) + count
    
    return answer


print(solution(3,[1,2],[2,3]))