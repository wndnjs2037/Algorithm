# 1181 단어 정렬
# sort -> 문자열도 정렬 가능, input()은 느림!

n = int(input())
words = []

for i in range(n): # 입력받은 만큼 반복
  words.append(input()) # 입력받은 단어를 words 리스트에 넣어줌

set_words = set(words) #중복값을 제거하기 위해 set화
words = list(set_words) #중복값을 제거한 단어들을 다시 list로 전환

words.sort() #정리된 단어들을 sort로 정렬
words.sort(key = len) # 길이가 같으면 처리

for i in words: #정렬된 단어들을 차례대로 출력
  print(i) 