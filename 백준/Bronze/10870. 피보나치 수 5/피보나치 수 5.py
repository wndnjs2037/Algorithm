# 10870 피보나치 수 5
# 재귀함수 사용하여 풀이

n = int(input())

def fibonacci(n):
  if n <= 1:
    return n # 입력받은 값이 1보다 같거나 작다면 n을 그대로 리턴

  return  fibonacci(n-1) + fibonacci(n-2) # n이 2 이상일 때 부터는 1과 0을 더하고, 3이면 1씩 증가하면서 재귀됨

print(fibonacci(n))