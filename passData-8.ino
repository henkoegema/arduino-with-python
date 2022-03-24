//Using an Arduino with Python LESSON 11: Controlling an LED from Python
//Input data from: ~/Documents/pyArduino/passData-8.py
//https://www.youtube.com/watch?v=VdSFwYrYqW0&t=682s

int redPin = 6;
int greenPin = 5;
int bluePin = 3;
//Common ANODE = +5V

int ON = 0;
int OFF = 255;

int redVal;
int greenVal;
int blueVal;

String cmd;

void setup() {
  Serial.begin(115200);
  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);
}

void loop() {
  while(Serial.available() == 0) {}

  redVal = Serial.readStringUntil(':').toInt();
  greenVal = Serial.readStringUntil(':').toInt();
  blueVal = Serial.readStringUntil('\r').toInt();

  analogWrite(redPin, 255 - redVal);
  analogWrite(greenPin, 255 - greenVal);
  analogWrite(bluePin, 255 - blueVal);

  
/*  cmd = Serial.readStringUntil('\r');
  
  if (cmd == "OFF"){
    analogWrite(redPin,OFF);
    analogWrite(greenPin,OFF);
    analogWrite(bluePin,OFF);
  }

  if (cmd == "RED"){
    analogWrite(redPin,ON);
    analogWrite(greenPin,OFF);
    analogWrite(bluePin,OFF);
  }

  if (cmd == "GREEN"){
    analogWrite(redPin,OFF);
    analogWrite(greenPin,ON);
    analogWrite(bluePin,OFF);
  }

  if (cmd == "BLUE"){
    analogWrite(redPin,OFF);
    analogWrite(greenPin,OFF);
    analogWrite(bluePin,ON);
  }

  if (cmd == "CYAN"){
    analogWrite(redPin,OFF);
    analogWrite(greenPin,ON);
    analogWrite(bluePin,ON);
  }

  if (cmd == "MAGENTA"){
    analogWrite(redPin,ON);
    analogWrite(greenPin,OFF);
    analogWrite(bluePin,ON);
  }

  if (cmd == "YELLOW"){
    analogWrite(redPin,ON);
    analogWrite(greenPin,ON);
    analogWrite(bluePin,OFF);
  }
*/
// EOF
}
