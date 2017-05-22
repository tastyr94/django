var timer,
 i = 0,
 divide = 100;


function start(){
 // setInterval()은 지정된 시간후 특정 자바스크립트 코드가 포함된 문자열을 반복하여 호출하는 메소드
 // 지정된 시간 increment() 함수를 의미

 timer = self.setInterval('increment()', (1000 / divide));
}

function increment(){
 // ( i / divide )??
 i++;
 document.getElementById('time_out').innerHTML = (i / divide);
}

function stop(){
 // clearInterval : setInterval을 멈출 때 사용
 // timer = null을 준 이유는?
 clearInterval(timer);
 timer = null;
}

function reset(){
 stop();
 i = 0
 document.getElementById('time_out').innerHTML = (i / divide);
}