def solution(phone_book):
  for i in range(len(phone_book)-1):
    for j in range(i+1,len(phone_book)-1):
      if phone_book[i].find(phone_book[j]):
        return False
      if phone_book[j].find(phone_book[i]):
        return False
  return True
    
     
print(solution(["123", "456", "789"]))