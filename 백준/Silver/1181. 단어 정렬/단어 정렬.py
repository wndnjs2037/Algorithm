# 1181 단어정렬 - 개선된 속도로 풀어보기

import sys #stdin 을 사용하기 위한 임포트

n = int(sys.stdin.readline())
words = []

for i in range(n): # 입력받은 만큼 반복
  words.append(sys.stdin.readline().strip()) 
  # sys.stdin.readline()은 '\n\'을 포함하는 입력이기 때문에 연속으로 값을 입력받는 for문에서 에러가 발생하므로
  # strip으로 끊어서 처리해준다.

set_words = set(words) #중복값을 제거하기 위해 set화
words = list(set_words) #중복값을 제거한 단어들을 다시 list로 전환

words.sort() #정리된 단어들을 sort로 정렬
words.sort(key = len) # 길이가 같으면 처리

for i in words: #정렬된 단어들을 차례대로 출력
  print(i)  
