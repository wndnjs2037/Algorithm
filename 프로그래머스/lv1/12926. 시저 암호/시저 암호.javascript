// 암호화 할 문자열 s를 입력받고 n만큼 거리를 민 암호문을 만드는 함수 만들기
// 1) 아스키코드 값을 이용하여 푸는 방법
// charCodeAt() : 해당하는 문자의 아스키 코드값을 반환해줌
// String.fromCharCode() : 해당하는 아스키 코드 숫자의 문자를 반환
// 즉, charCodeAt() -> String.fromCharCode() 의 과정을 거쳐서 아스키 코드값을 받았다가 문자로 변환하여 최종 출력

function solution(s, n) {
    // 결과 값을 리턴에 바로 적어주는 방식 사용
    return s.split("").map(value => { //입력받은 문자열 s를 ""으로 분리한 뒤, value라는 이름의 요소로 하나씩 넣어주고(배열화)
        if (value == " ") return value; //빈 값을 입력받는다면 그대로 빈 값 리턴
        // 삼항연산자 사용
        return value.toUpperCase().charCodeAt() + n > 90 ? 
        // value를 대문자로 변경한 값의 아스키 코드에 n만큼 값을 더해서
        // 해당 값이 90(Z, 알파벳 문자열의 끝)을 넘어가는지를 조건으로 걸고
            String.fromCharCode(value.charCodeAt() + n - 26) // Z를 넘는다면(90보다 크다면) 다시 A부터 시작하기 위해 
            // -26 (알파벳 개수)만큼 차감하여 A부터 계산하게 한다.
            : String.fromCharCode(value.charCodeAt() + n) // Z를 넘지 않는다면 입력받은 n 만큼 미뤄준다.
            
    }).join(""); //위의 과정을 거친 value 요소들을 join을 통해 하나의 문자열로 묶어준다. 
}