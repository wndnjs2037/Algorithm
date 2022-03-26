a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c)) #리스트에 결과 값을 한 글자씩 쪼개서 넣어주고

for i in range(10): #10번 반복해서(0~9)
    print(result.count(str(i))) #count 함수를 사용해서 해당 리스트에 문자(0~9)가 몇개씩 있는지 출력
