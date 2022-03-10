#2525 오븐 시계 - 구글 참고

H, M = map(int, input().split()) #현재 시각
timer = int(input()) #요리에 필요한 시간

H = H + timer // 60 #60으로 나눈 몫(정수 값)만큼 시간에 더해줌
M = M + timer % 60 #60으로 나눈 뒤 나머지 값을 분에 더해줌

if M >= 60: #분이 60을 넘어가는 경우
  H = H + 1 #시간에 1을 더하고
  M = M - 60 #분에서는 60을 제외한 값으로 세팅

if H >= 24: #시간이 24를 넘어가는 경우
    H =  H - 24 #해당 시간에서 24만큼을 빼서 다시 세팅

print(H, M)