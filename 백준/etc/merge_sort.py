# 2751 수 정렬하기2 - O(nlogn) : 병합, 힙정렬 등
# 재귀를 이용한 병합 정렬
# 병합정렬 함수만 미리 만들어둠!

def merge_sort(arr):
  if len(arr) < 2: # 정렬할 어레이의 길이가 2보다 작다면 (요소가 1개라면)
    return arr #어레이를 그대로 리턴
  
  mid = len(arr) // 2 # 병합정렬의 시작인 2로 나누기!
  low_arr = merge_sort(arr[:mid]) # 2로 나눈 후, 처음부터 나눈 부분 까지는 low 어레이로 담고
  high_arr = merge_sort(arr[mid:]) # 나머지 뒷부분은 high 어레이에 담아준다.

  merged_arr = [] # 병합정렬 완료된 데이터를 넣을 리스트
  l = h = 0

  while l < len(low_arr) and h < len(high_arr): # l이 low보다 작고, h가 high보다 작다면
    if low_arr[l] < high_arr[h]: #low arr의 요소가 high arr의 요소보다 작다면
      merged_arr.append(low_arr[l]) #해당 요소를 병합정렬 완료 리스트에 추가해준다.
      l += 1 #다음 요소를 확인하기 위해 l 값 증가시키기

    else : # low arr의 요소가 high arr의 요소보다 크다면
      merged_arr.append(high_arr[h]) #high arr의 요소를 병합정렬 완료 리스트에 추가해준다.
      h += 1 #다음 요소를 확인하기 위해 h 값 증가시키기

    # 즉, 위의 if-else 코드에서는 크기 확인이 완료된 arr의 요소를 한칸씩 뒤로 옮겨가면서 
    # 나뉘어진 어레이들의 요소들을 비교하여 merged_arr에 요소를 추가해준다.

  merged_arr += low_arr[l:] 
  merged_arr += high_arr[h:] #위의 if else에서 걸러지지 않은 뒷부분을 그대로 붙여줌

  return merged_arr #최종적으로 정렬 완료된 merged_arr를 리턴해준다
