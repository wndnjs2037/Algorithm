# 1316 그룹 단어 체커

n = int(input())

group_word = 0 #그룹 단어 개수를 체크할 변수 생성

for _ in range(n): #입력받은 단어 개수만큼 반복
  word = input() # 그룹 단어를 셀 word 입력받기
  error = 0
  for index in range(len(word)-1): # 인덱스 범위 생성 : 0부터 단어개수 -1 까지
    if word[index] != word [index+1] : # 이웃해있는(연달은) 두 문자가 다른 경우
      new_word = word[index+1:] # 현재 글자 이후의 문자열을 새로운 단어로 생성
      if new_word.count(word[index]) > 0 : #남은 문자열에서 현재 글자가 있다면
        error += 1 #에러 값에 1씩 증가
  
  if error == 0:
    group_word += 1
  
print(group_word)

# 다시 풀어보기