// 입력받은 숫자를 분해해서 각각 더한 값을 반환하기

function solution(n)
{
    let arr = n.toString().split("").map(x => parseInt(x));
    // 입력받은 n을 toString을 통해 문자열로 만들고, split()으로 분해한 뒤
    // map을 사용해서 10진수로 변경한다.
    // parseInt() -> 문자열을 정수(Int)로 변환시켜주는 함수
    
    return arr.reduce((acc, cur) => acc + cur, 0);
    // 배열의 각 요소들을 누적해서 더해야 하기 때문에 reduce() 사용
    // reduce() 배열의 요소들을 순회하며 반복적인 연산 수행을 하는데,
    // 누산값을 계산해주는 역할을 한다.
    // acc : 누산값
    // cur : 현재 요소값
    // acc + cur : 다음 누산값
    // 0 : 초기 누산값
    
}