# 2908 상수

A, B = map(str, input().split())

reverse_A = A[2] + A[1] + A[0]
reverse_B = B[2] + B[1] + B[0]

if int(reverse_A) > int(reverse_B):
  print(reverse_A)

else :
  print(reverse_B)