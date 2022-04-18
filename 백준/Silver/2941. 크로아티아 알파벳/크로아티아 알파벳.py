# 2941 크로아티아 알파벳
# 문자열 치환하기만 하면 될듯
# replace 함수 사용

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in croatia:  #크로아티아 문자 리스트를 돌면서 i가 리스트 안에 있으면 * 한글자로 변경해줌
  s = s.replace(i, '*') #인풋 변수와 동일한 이름의 변수 


print(len(s))