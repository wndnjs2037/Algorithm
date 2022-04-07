# 10809 알파벳 찾기 - 구글링

S = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc : #알파벳을 i에 담아 한 개(char)씩 가져옴
    if i in S : #i가 S안에 들어있다면,(여기서 i는 abc 안을 돌며 a b c 한 자씩 가져오는 이터레이터)
        print(S.index(i), end=' ') # S의 i번째 인덱스를 출력해줌
    else:
        print(-1, end=' ') #아니라면 -1 삽입