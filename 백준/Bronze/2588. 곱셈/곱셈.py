#2588 곱셈

input1 = int(input()) # 곱셈연산을 할 세자리 수 변수 두개 입력받기
input2 = input()
p1 = int(input2[:1]) #두번째로 입력받은 숫자의 첫번째 자리 숫자 추출
p2 = int(input2[1:2]) #두번째 자리 숫자 추출
p3 = int(input2[-1:]) #세번째 자리 숫자 추출

output3 = input1 * p3 #3번 자리 값 구하기
output4 = input1 * p2 #4번 자리 값 구하기
output5 = input1 * p1 #5번 자리 값 구하기
input2 = int(input2)

output6 = (input1 * input2)
print(output3, output4, output5, output6, sep='\n')