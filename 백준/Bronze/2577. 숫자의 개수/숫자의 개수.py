# 2577 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_list = list(map(int, str(result))) #int로 변환할 것이므로 int를 적고, 적용할 값은 str으로 변경하여 넣어준다.
#print(result_list)
#print(len(result_list))

count0,count1,count2,count3,count4,count5,count6,count7,count8,count9 = 0,0,0,0,0,0,0,0,0,0

for i in range(0, len(result_list)):
  if result_list[i] == 0:
    count0 += 1

  elif result_list[i] == 1:
    count1 += 1
  
  elif result_list[i] == 2:
    count2 += 1

  elif result_list[i] == 3:
    count3 += 1
  
  elif result_list[i] == 4:
    count4 += 1
  
  elif result_list[i] == 5:
    count5 += 1
  
  elif result_list[i] == 6:
    count6 += 1

  elif result_list[i] == 7:
    count7 += 1
  
  elif result_list[i] == 8:
    count8 += 1

  elif result_list[i] == 9:
    count9 += 1

print(count0)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)
