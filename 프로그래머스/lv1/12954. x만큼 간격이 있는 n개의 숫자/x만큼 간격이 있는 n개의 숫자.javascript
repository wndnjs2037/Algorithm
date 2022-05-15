function solution(x, n) { // x는 시작할 값, x만큼 증가하는 값, n은 몇개를 출력할 것인지
    var answer = []; //결과를 담을 배열 선언
    
    for (let i = 1; i <= n; i++){  // i는 1부터 시작, n보다 작을 때 까지 +1 씩 증가하며 반복한다
        answer.push(x*i); //i는 1씩 증가하며 x와 곱해진다
        //배열(answer)에 데이터값을 넣을 떄는 push를 사용한다.
    }
    return answer;
}