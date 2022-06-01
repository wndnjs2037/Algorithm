// 배열 중 가장 작은 수를 제거하고 나머지 요소를 그대로 반환
// 작은 수를 제거한 배열이 빈 배열인 경우 -1 반환
// 입력 받은 배열 중 indexOf와 Math.min을 사용해서 
// 가장 작은 값과 그 값의 인덱스를 찾아낸 뒤 splice를 사용해 제거
// 작은 수를 제거한 배열이 빈 배열인지는 삼항 다항식으로 확인

// splice() : 배열의 기존 요소를 삭제 or 교체 or 새 요소 추가하여 배열 내용 변경, 원본 배열 자체를 수정한다.

const solution = (arr) => { 
    arr.splice(arr.indexOf(Math.min(...arr)), 1);
    
    // Math.min(...arr) : 배열의 최소값 찾기
    // 최소값을 찾아 indexOf로 인덱스를 구해 1개의 값을 splice로 삭제
    
    return arr.length? arr : [-1]; //  arr의 길이가 0이라면 false 이므로 -1 리턴, 0이 아니라면 true이므로 arr의 값을 리턴
};
    