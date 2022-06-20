// 입력받은 자연수 n을 뒤집은 순서로 배열의 요소로 넣어 반환하기
// n을 슬라이스해서 하나씩 map으로 저장
// reverse() : 배열의 순서를 거꾸로 만들어 주는 함수

function solution(n) {
    let answer = [];
    
    // n을 String으로 만들고, 하나씩 split해서 map으로 배열화
    // parseInt를 통해 요소들의 데이터형을 Int형으로 변환
    map1 = n.toString().split("").map(x=>parseInt(x));
    answer = map1.reverse()
    
    //console.log(answer) //확인용
    
    return answer;
}