#1546 평균
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
count = 0

for i in range(n):
  count += (scores[i] / m) * 100 
  

print(count/n)
