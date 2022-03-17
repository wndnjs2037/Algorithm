#10871 X보다 작은 수

N, X = map(int, input().split())

A = []
A = list(map(int, input().split())) #제한적으로 입력받는 부분 구현 해야할지..?

for i in range(N):
  if A[i] < X :
    print(A[i], end=" ")
