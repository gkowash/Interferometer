void setup() {
  //left = A0
  //middle = A1
  //right = A2
  //trigger = D2
  //LED = D4
  pinMode(4, OUTPUT);
  Serial.begin(500000);
}

void loop() {
  String spacer1 = ": ";
  String spacer2 = ", ";
  
  if(digitalRead(2) == HIGH){
    float timer_start = millis();
    digitalWrite(4, HIGH);
    while(millis()-timer_start < 2000){
      if(millis()-timer_start > 500){
        digitalWrite(4, LOW);
        }
      if(millis()-timer_start > 1000){
        digitalWrite(4, HIGH);
        }
      if(millis()-timer_start > 1500){
        digitalWrite(4, LOW);
        }
      }

        
    float start = micros();
    float interval = 20.0 * 1000000;
  
    while((micros()-start) < interval) {    
      int leftSensor = analogRead(A0);
      int middleSensor = analogRead(A1);
      int rightSensor = analogRead(A2);
      float leftVoltage = leftSensor*(4.81/1023.0);
      float middleVoltage = middleSensor*(4.81/1023.0);
      float rightVoltage = rightSensor*(4.81/1023.0);
  
      String output = (micros()-start)/1000 + spacer1 + leftVoltage + spacer2 + middleVoltage + spacer2 + rightVoltage;
      Serial.println(output);
    }
  }
}
