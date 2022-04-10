# 1157 단어공부

word = input().lower() # 입력받은 문자열을 모두 소문자로 치환하여 통일화
word_list = list(set(word)) #입력받은 word를 set타입으로 변환하여 중복 값을 제거한 뒤, 정제된 값을 리스트로 생성한다.
cnt = [] #결과를 담을 빈 리스트 생성

for i in word_list: # i는 정제된 word_list의 값을 하나씩 순회하는 이터레이터 
  count = word.count(i) #문자열 정제 전 입력된 그대로의 단어를 i가 순회하며 개수를 세어서 count에 넣는다.
  # 예를 들어, test가 입력되었다면 정제된 값 -> t,e,s / 정제전 값 ->test
  # i는 t,e,s가 되고, test라는 문자열에서 t가 몇번인지, e가 몇번인지, s가 몇번인지 count 함수로 세어 count 변수에 대입한다.
  cnt.append(count) #문자를 센 값 count를 cnt 리스트에 추가해준다.

if cnt.count(max(cnt)) >= 2: # 만약 cnt 리스트 안의 가장 큰 값(max)를 세었을 때(count), 센 개수의 값이 cnt 리스트 안에 2개 이상이라면(중복이라면)
  # -> 즉 max(cnt) 값이 2개 이상이라면 실행
  print('?') #물음표 출력

else: 
  #cnt에는 알파벳이 등장한 숫자 데이터만 저장이 된다.
  # print(cnt) -> 숫자가 들어있는 데이터
  # print(max(cnt)) -> 해당 데이터에서 최대값
  # print(cnt.index(n)) -> 위와 동일한 값

  print(word_list[(cnt.index(max(cnt)))].upper()) 
  # cnt.index(max(cnt)) -> 가장(max) 빈번하게 나온 알파벳의 횟수를 index()함수의 인자로 넣어서 cnt 안의 알파벳 개수의 값(숫자)을 가져옴
  # 가져온 값으로 word_list(정제된 리스트)에서 알파벳을 최종적으로 가져와 대문자로 치환해준다.
  