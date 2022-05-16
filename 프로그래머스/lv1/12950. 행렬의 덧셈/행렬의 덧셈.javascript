// 2차원 배열을 for문으로 돌려서 2개의 배열을 같은 인덱스끼리 덧셈


function solution(arr1, arr2) { //입력받는 두 arr의 길이는 같다.
    var answer = []; //답을 넣을 배열 선언
    
    for(let i = 0; i <arr1.length; i++){ 
        let sum = []; //더한 값을 넣을 배열 선언
        
        for(let j = 0; j<arr1[i].length; j++){ //arr1 안의 배열의 길이 (2번) - [1,2], [2,3]
            sum.push(arr1[i][j] + arr2[i][j]) //arr들의 값 위치에 맞게 서로 더해줌 - 1+3 , 2+4, 2+5, 3+6
            // 더한 값은 sum 배열에 push로 저장한다.
            
        }
        answer.push(sum) //저장한 값은 answer에 대입
    }
    
    return answer; //최종 답 리턴
}

//ansswer 하나만 사용하는 방법으로도 풀어보기