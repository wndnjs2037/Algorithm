# 5622 다이얼

dial = [ 'ABC', 'EDF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

#dial.index('ABC')

time = 0 
for dial_set in dial:
  #print(dial_set) # -> ABC EDF ...
  for dial_one in dial_set: # 알파벳 리스트에서 각 요소를 꺼내서 한글자 씩 분리
    #print(dial_one) # -> A B C D ...
    for x in word: # 입력받은 문자열의 문자를 하나씩 가져옴
      if x == dial_one: # 입력받은 문자열의 문자와 알파벳 리스트의 문자가 같다면
        time += dial.index(dial_set) + 3 # 걸리는 시간을 time에 담음


print(time)