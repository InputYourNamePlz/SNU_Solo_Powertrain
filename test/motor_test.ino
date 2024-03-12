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
