// 배열의 합계와 평균을 구하는 방법 : reduce() 사용
// reduce를 통해 배열의 합을 구한 뒤, 배열의 길이만큼 나누어서 평균값 계산

function solution(arr) {
    
    // 결과를 담을 상수 변수 result 선언 후
    // 함수의 인자로 받은 arr에 reduce 함수를 통해 합계를 구함
    const result = arr.reduce(function add(sum, currValue) {
        return sum + currValue;
    }, 0);
    
    // 배열의 합계값을 배열의 길이(요소의 갯수)로 나누어 평균값 구하기
    const average = result / arr.length;
    
    //console.log(average);
    
    return average;
}