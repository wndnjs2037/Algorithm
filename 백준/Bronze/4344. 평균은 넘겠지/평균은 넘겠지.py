# 4344 평균은 넘겠지

c = int(input()) # 테스트 케이스 개수 

for _ in range(c):
  nums = list(map(int, input().split())) #입력받은 값을 리스트에 저장
  avg = sum(nums[1:])/nums[0] # 평균을 구함 (nums[0] => 학생 수, nums[1:] => 1번째 인덱스부터 끝까지, 즉 점수 값들)
  cnt = 0
  for score in nums[1:]: #학생들의 점수만큼 반복문 실행
    if score > avg: #score의 요소의 값이 avg보다 크다면
      cnt += 1 #카운트에 1씩 증가하여 평균을 넘는 학생의 수를 구함

  rate = cnt/nums[0] * 100 #비율을 구하기 위해 평균이상 학생 수 /전체 학생수 * 100
  print(f'{rate:.3f}%')