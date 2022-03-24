# 문자열 슬라이싱을 이용한 코드

string = input()
alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp = ''

for i in string:
    temp = temp + alpabet[alpabet.index(i)-3] #index 함수를 사용해서 stirng에 입력된 문자가 몇번째에 위치해있는지 구한 뒤,
    # 해당 값에 -3을 해준다. (3만큼 이동하여 암호화하므로)

print(temp)
    