# 2439 별 찍기 - 2

n = int(input())
i = 1
for i in range(1,n+1):
  print(" "* (n-i) + "*"*(i))