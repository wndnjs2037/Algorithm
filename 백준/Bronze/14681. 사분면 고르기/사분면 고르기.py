#14681 사분면 고르기

x = int(input())
y = int(input())

if x >= 1 and y >= 1:
  print(1)
elif x >= 1 and y <= 1:
  print(4)
elif x <= 1 and y <= 1:
  print(3)
elif x <= 1 and y >= 1:
  print(2)