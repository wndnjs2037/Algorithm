// 입력받은 값 n을 내림차순으로 정렬하기
// 내장 메서드 sort() 활용

function solution(n) {  
    return Number(n.toString().split("").sort((a,b)=> b-a).join(""))
    // 파라미터로 입력받은 n을 toSting()을 사용하여 문자열로 변환한 다음
    // 한 글자씩 split("")해서 배열로 변경한 뒤
    // sort()를 사용하여 내림차순으로 정렬한다. 
    // (여기서 return 값 a-b는 배열을 오름차순, b-a는 내림차순으로 정렬한다.)
    // 정렬된 값을 join("")을 통해 이어진 문자열로 변경해주고
    // Number()를 통해 문자를 숫자로 변경한다.
}