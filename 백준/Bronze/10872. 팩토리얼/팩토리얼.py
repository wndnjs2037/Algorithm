# 10872 팩토리얼
# 재귀 함수 코드

def factorial(n):
  result = 1 # result 변수를 1로 초기화
  if n > 0 : # 만약 입력받은 값이 0보다 크다면 
    result = n * factorial(n-1) #결과 변수에 해당 값 * 해당값-1 의 팩토리얼 값을 넣어서 재귀 함수 사용
  return result #결과 출력

n = int(input())
print(factorial(n))