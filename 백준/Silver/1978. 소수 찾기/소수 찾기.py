# 1978 소수찾기
# 소수 = 자기자신 외에는 어떠한 수로도 나누어지지 않는 수
# 특정 수 n이 소수인지 아닌지 구하는 방법 : 2부터 n-1까지의 수로 해당 수를 나누고, 나누어 떨어지면 소수가 아님

n = int(input())
numbers = list(map(int, input().split()))
prime = 0

for num in numbers:
  notPrimeNum = 0 
  if num > 1: #1 이상의 숫자만 판별
     
    for j in range(2, num):
      if num % j == 0:
        notPrimeNum += 1 #소수가 아니므로 아닌 변수에 증가

    if notPrimeNum == 0: #소수가 아닌 경우에 포함되지 않는 경우
      prime  += 1
    
   
print(prime)