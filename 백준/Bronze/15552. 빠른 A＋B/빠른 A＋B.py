import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline()) #시간 제한에 걸리지 않는 방식으로 테스트 케이스 입력받기

for i in range(t): #입력받은 테스트케이스 수 만큼 반복
    a, b = map(int, sys.stdin.readline().split()) #a와 b를 입력받고
    print(a+b) #더한 값을 출력