process.stdin.setEncoding('utf8'); // 문자인코딩 방식 설정
process.stdin.on('data', data => { // 입력받은 숫자를 data에 받음
    const n = data.split(" "); //data를 배열로 변경, 즉 입력받은 숫자를 배열 형태로 저장한다. ex) 5 3 
    const a = Number(n[0]);
    const b = Number(n[1]); 
    // a는 한 줄에 대한 별의 갯수, b는 몇 줄 출력할지에 대한 값
    // 배열로 변경한 값 중 앞에 값은 a에, 뒷 값은 b에 넣어줌
    
    for(let i = 0; i<b ; i++){ // 몇줄 반복할지, b보다 작을 때 까지 반복
        let str = "" //출력할 변수
        for(let j = 0; j<a; j++){ //한 줄에 별을 몇개 찍을지, a보다 작을 때 까지 반복
            str = str + "*" //출력할 변수에 별을 담아줌
        }
    console.log(str);
    }
    
});