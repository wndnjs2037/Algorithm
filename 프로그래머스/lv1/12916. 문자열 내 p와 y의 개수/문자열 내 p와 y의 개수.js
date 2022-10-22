function solution(s){
    // s로 받은 문자열을 모두 대문자로 변경한 뒤
    // P와 Y로 스플릿한 결과의 길이가 같으면 T, 틀리면 F 반환
    
    return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
}