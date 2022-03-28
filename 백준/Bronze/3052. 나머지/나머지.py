#3052 나머지

numbers = []

for i in range(10):
  N = int(input())
  numbers.append(N%42)

numbers = set(numbers) #중복 값 삭제
print(len(numbers))