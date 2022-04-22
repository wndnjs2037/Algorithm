# 2750 수 정렬하기

n = int(input())
numbers = []

for i in range(n):
  number = int(input())
  numbers.append(number)

numbers.sort()

for num in numbers:
  print(num)
