// 하샤드 수의 규칙과 출력 조건
// 18 = 1 + 8 = 9 => 자리수의 합 9
// 18 % 9 = 0 => 하샤드 수 True
// 이를 공식화하면, ab = a + b = sum(a,b)
// ab % sum(a,b) = 0 => True, 1이면 False
// % 나머지 연산을 사용하여 0인 경우에 True 출력하기

function solution(x) {
    let sum = 0;
    let arr = String(x).split("") //입력받은 숫자를 자리수 별로 split 하여 arr이라는 배열에 담는다
    
    //split한 arr의 길이만큼 반복하는 반복문 생성
    for(let i=0; i<arr.length; i++){
        sum += Number(arr[i]) // sum에 split한 자릿수를 각각 누적해서 더해준다.
        // 즉, 입력받은 x의 자릿수의 합을 구하는 과정
        
    }
    //입력받은 값 x를 자릿수의 합인 sum으로 나눈 나머지가 0이라면 ture, 아니라면 false를 리턴하도록 설정
    return (x % sum == 0) ? true:false;
    // 간단한 조건문은 위와 같은 삼항연산자가 가독성이 뛰어나다.
}