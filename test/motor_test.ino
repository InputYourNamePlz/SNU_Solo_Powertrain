///////////////////
// 실제로 자동차용 코드
// 이렇게 대충 만들었다간
// 사람 목숨 날라갑니다!!!
// 말 그대로 모터 돌리기만
// 할 수 있는 코드임
//
// 실제 자동차용 코드는
// 값을 이중 삼중으로
// 검사해야함
///////////////////

int outputPin = 5;
int pwm = 0;

void setup() {
  Serial.begin(115200);
  pinMode(outputPin, OUTPUT);
}

void loop() {

  if (Serial.available()) {

    input_data = Serial.readStringUntil('\n');

    pwm = input_data.toInt();
    if (pwm > 255) {
      pwm = 255;
    } else if (pwm < 0) {
      pwm = 0
    }

    analogWrite(outputPin, pwm);
  }
}
}
