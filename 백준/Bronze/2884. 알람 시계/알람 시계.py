#2884 알람시계 - 구글 참고

h, m = map(int, input().split()) #시간과 분을 입력받고

if m < 45 : #입력받은 분이 45보다 작으면
  if h == 0 : #시간이 0 시이면
    h = 23 #23시로 다시 설정
    m = 60 + m #시간단위가 변경되므로 다시 60에서 분을 빼줌
  else : #0시가 아니라면
    h = h - 1 #시간단위 -1
    m = 60 + m #시간단위가 변경되므로 다시 60에서 분을 빼줌
    
print(h, m-45) #프린트 시에 45를 제외해서 출력