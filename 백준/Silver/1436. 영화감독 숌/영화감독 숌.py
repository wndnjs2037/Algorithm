from sys import stdin
n = int(stdin.readline())
x = 666

while (1):
    if (str(x).find('666') != -1):
      n -= 1 
    if (n == 0):
        break
    x = x + 1

print(x)
