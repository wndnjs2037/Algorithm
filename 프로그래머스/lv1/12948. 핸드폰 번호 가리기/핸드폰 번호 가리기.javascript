// 뒤에서부터 4자리를 제외하고 앞의 문자열은 *로 치환하는 방법
// repeat() : 지정한 횟수만큼 문자열 반복 출력
// slice() : 마지막 4자리의 문자를 자르는 용도

function solution(phone_number) {
    
    let answer = "*".repeat(phone_number.length -4) + phone_number.slice(-4);
    return answer;
}