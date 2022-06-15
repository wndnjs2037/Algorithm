function solution(s) {
    // 결과값 바로 리턴
    return s.split(' ').map(word => { //공백을 기준으로 단어를 나눈 뒤
        let result ='';// 값을 저장할 변수 선언
        for(let i=0; i < word.length; i++) { //단어의 길이만큼 반복하는 for문
            if(i%2) { //해당 단어의 위치가 홀수 인덱스라면(1이면 True가 되어 아래 문장이 실행됨)
                result += word[i].toLowerCase(); //소문자로 변환하여 result에 저장
            } else { //해당 단어의 위치가 짝수 인덱스라면
                result += word[i].toUpperCase(); //대문자로 변환하여 result에 저장
            }
        }
        return result; //연산한 결과를 리턴해준다.
    }).join(' '); //결과를 리턴받아 공백을 포함하여 join해줌
}