# 1427 소트인사이드
# 값을 입력받은 뒤 내림차순 정렬하기

n = list(map(int, input()))

n.sort(reverse=True)

for num in n:
  print(num, end='')