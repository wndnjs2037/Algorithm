#2480 주사위

a, b, c = map(int, input().split())

if a == b == c :
  print(10000 + a * 1000)

elif a == b or b == c or a == c:
  if a == b :
    print(1000 + a * 100)
  elif b == c :
    print(1000 + b * 100)
  elif c == a :
    print(1000 + c * 100)

elif a != b and b != c and c != a:
  m = max(a, b, c)
  print(m * 100)