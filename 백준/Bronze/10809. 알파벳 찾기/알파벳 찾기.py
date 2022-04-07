# 10809 알파벳 찾기 - 다시풀기 (순서 수정)

s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:  #알파벳 문자열을 하나씩 가져와서 i에 담아 비교
  if i in s: #입력받은 문자열에 알파벳이포함되어 있으면 
    #print("i :", i)
    #print("j : ",j)
    print(s.index(i), end=' ') #s에 해당 알파벳 i가 포함되어 있는 위치(s의 인덱스)를 출력

  else:
    print(-1, end=' ') # 그 외에는 -1을 출력
      