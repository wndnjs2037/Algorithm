# 2675 문자열 반복

t = int(input())

for test in range(t):
  R, S = map(str, input().split())
  
  for i in S:
    print(i *int(R), end='')
  
  print()