function solution(n) {
    let answer = 0; //결과를 담을 변수
    
    for (let i = 0; i <= n; i++) { //입력받은 n 만큼 반복하는 for문
        if( n % i === 0 ) { // 입력값 n을 0부터 n(i값)으로 나누었을 때 나머지거 0이라면 == 약수라면
            answer += i; // answer에 해당 i값을 누적해서 더해준다
        }
    }
    return answer; //최종으로 누적된 값을 리턴함
}