import sys #빠른 입력을 받기 위한 sys 임포트
sys.setrecursionlimit(10 ** 6)

# 파이썬의 기본 재귀 제한은 1000으로 매우 얕은 편,
# 재귀로 코테문제를 풀 때에는 위의 설정을 꼭 적어주자!

def append_star(LEN):
    if LEN == 1: # 입력된 값이 1이라면 별 하나만 출력
        return ['*']

    Stars = append_star(LEN // 3) # 입력된 값을 3으로 나누어서 함수 재호출
    L = [] # 값을 담을 빈 리스트 생성

    # 공간을 3개의 줄로 나누고, 재귀를 통해 구해진 별의 개수만큼 붙여서 리스트에 추가해준다
    for S in Stars: # 첫번째 라인은 
        L.append(S * 3) # 꽉 채워져 있으므로 3을 곱함
    for S in Stars: # 두번째 라인은 
        L.append(S + ' ' * (LEN // 3) + S) # 빈칸을 가운데에 넣어준다
    for S in Stars: # 세번째 라인은 첫번째와 동일
        L.append(S * 3)
    return L # 완성된 리스트를 리턴해줌


n = int(sys.stdin.readline().strip()) # 사용자에게 입력값을 받는다
print('\n'.join(append_star(n))) # \n을 기준으로 값을 join하여 프린트한다

 
