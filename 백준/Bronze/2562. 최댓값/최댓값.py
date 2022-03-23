# 2562 최댓값

numbers = []
count = 0

for i in range(9): #9개의 자연수 입력받기
  N = int(input())
  numbers.append(N)

for j in range(len(numbers)):
  if numbers[j] == max(numbers):
    print(numbers[j])
    print(j+1)