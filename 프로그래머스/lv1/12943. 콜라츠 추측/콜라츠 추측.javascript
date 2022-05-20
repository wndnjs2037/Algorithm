// num이 짝수라면 / 2
// num이 홀수라면 * 3 + 1
// num == 1 이 될 때 까지 반복
// count == 500이 되면 -1 반환
// num 이 1이 되면 함수 종료 후 count 리턴

function solution(num) {
    let count = 0;
    
    while(num != 1){
    	if ((num % 2) == 0) { //num이 짝수라면 수행할 조건문
    		num = num / 2;
      	count = count + 1;
    	}
    	else if((num % 2) == 1){ //num이 홀수라면 수행할 조건문
    		num = (num * 3) + 1;
      	count = count + 1;
    	}
      
    	if(count >= 500){	//작업 횟수가 500을 넘어간다면 수행할 조건문
        return -1;
    	}
    }
    return count;
}