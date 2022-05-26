function fibonacci(n){
    let fNum = [0,1,1];
    for (let i = 3; i <= n; i++) { // 0과 1은 제외하고, 3부터 입력값 까지 반복되는 반복문
        fNum[i] = (fNum[i - 1] + fNum[i - 2])%1234567;
        //피보나치 수식이 적용된 수를 더해서 구한 뒤 123456로 나누어준다.
    }
    return fNum[n];
}

function solution(n) {
    const answer = fibonacci(n) % 1234567; //다시 1234567로 나누어줌
    return answer;
    
}