int potPinBl = A1;
int potPinGe = A2;
int potPinRo = A0;

int potValBl;
int potValGe;
int potValRo;
int DL = 100;


void setup() {
  pinMode(potPinBl,INPUT);
  pinMode(potPinGe,INPUT);
  pinMode(potPinRo,INPUT);
  
  Serial.begin(115200);

}

void loop() {
  potValBl = analogRead(potPinBl);
  potValGe = analogRead(potPinGe);
  potValRo = analogRead(potPinRo);
  
  Serial.print(potValBl);
  Serial.print(',');
  Serial.print(potValGe);
  Serial.print(',');
  Serial.println(potValRo);
  delay(DL);
}
