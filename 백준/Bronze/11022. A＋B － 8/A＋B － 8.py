# 11022 A+B - 8

t = int(input())

for i in range(0, t):
  a, b = map(int, input().split())
  print(f"Case #{i+1}: {a} + {b} = {a+b}")