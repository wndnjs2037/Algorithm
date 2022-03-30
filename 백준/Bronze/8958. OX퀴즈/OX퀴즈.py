n = int(input())

for i in range(n):
  inputString = input()
  strings = list(inputString)

  sum = 0 #점수를 합산해서 저자할 변수
  score = 1 # O와 X에 따라 나뉘는 점수

  for i in strings: # i는 string에 입력된 요소들을 하나씩 가져옴
    if i == 'O': # i가 O를 만나면 sum에 점수를 1 더해주고
      sum = sum + score # 누적할 점수는 1부터 시작해서 O가 있을수록 증가하는 score를 더해줌
      score = score + 1
    
    else: #X라면 점수를 초기화하기 위해 다시 1로 설정
      score = 1
  print(sum)