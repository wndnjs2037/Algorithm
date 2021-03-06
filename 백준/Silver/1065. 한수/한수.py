# 1065 한수
# 등차수열 : 연속하는 두 항의 차이가 모두 일정한 수열을 뜻한다. 예를 들어 1, 3, 5, 7, 9, ... 은 등차수열이다.
# 공차 : 공통적으로 나타나는 차이의 값, 위의 예시에서는 공차 2
# https://www.acmicpc.net/board/view/25689 참고
# 만약에 N이 130이 주어졌다면 1부터 130까지의 수 각각에 대해 그 수를 구성하는 수가 등차수열을 만족하는지 보면 된다
# 1~9 는 모두 한수에 포함된다!

n = int(input()) 
hansu = 0

for i in range(1, n+1): #1부터 입력받은 값 +1 까지 반복
  if i <= 99 : #1부터 99까지는 모두 한수이다.
    hansu += 1 # n이 99보다 작거나 같으면 hansu에 1씩 더해준다

  else :
    nums = list(map(int, str(i))) #n=100 이상부터는 str화 한 뒤 숫자를 자릿수대로 분리하여 리스트에 저장한다.
    if nums[0] - nums[1] == nums[1] - nums[2] : 
      #예를 들어, 111의 경우 1 - 1 == 1 - 1 의 값이 같으므로 등차수열이고,
      # 이런 경우에 해당되도록 if 조건을 걸어준다. -> 이 경우에는 한수이므로 hansu에 +1을 해준다.
      hansu += 1

print(hansu)
