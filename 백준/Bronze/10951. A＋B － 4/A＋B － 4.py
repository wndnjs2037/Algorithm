# 10951 A+B - 4
# 런타임 에러 이유를 몰라서 구글 참고

while True:
    try: #A와 B에 int형이 들어간다면 더한 값을 출력
        A, B = map(int, input().split()) 
        print(A+B)
    except: #try에 대한 에러가 발생한 경우 (int 가 아닌 경우) while문 중단
        break