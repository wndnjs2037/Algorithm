// Math.sqrt() : 제곱근을 구해주는 math 메소드
// 정수인지 아닌지 판단하는 방법 2가지
// 1) Number.inInteger() : 파라미터로 입력받은 값이 정수인지 판단함
// 2) 정수는 1로 나눈 경우 나머지가 항상 0인 속성이 있다.

function solution(n) {
    let num = Math.sqrt(n); //입력받은 n의 제곱근 값 구함
    if(num%1 === 0) // 제곱근을 1로 나누어서 나머지가 0이라면 == 정수라면
        return (num+1) * (num+1)
    else //아니라면
        return -1

}