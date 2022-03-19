# 1110 더하기 사이클 - 구글링 참고
n = int(input())
num = n
cycle = 0

while 1 :
  fisrt = num // 10 #10으로 나눈 뒤의 몫이므로 2자리 입력시 10의 자리가 반환
  second = num % 10 # 10d으로 나눈 뒤의 나머지이므로 2자리 입력시 1의 자리가 반환
  plus = (fisrt + second) % 10 # 첫째자리와 둘째자리를 더한 값을 10으로 나눈 뒤의 나머지(1의 자리, 맨 오른쪽 자리)를 plus에 저장
  num = (second * 10) + plus #입력받은 1의 자리에 10을 곱해 10의 자리 숫자로 만들고, plus에 담아두었던 1차 덧셈의 오른쪽 자리 숫자를 더해줌

  cycle += 1 #사이클이 한 번 돌았으므로 +1

  if( num == n ): # 처음에 입력한 n과 계산한 num이 같아지면 while문 탈출
    break

print(cycle)