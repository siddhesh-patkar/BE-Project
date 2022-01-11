void setup() {
  // put your setup code here, to run once:
pinMode(A0,INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int mq = analogRead(A0);
  Serial.print("Airquality = ");
  Serial.print(mq);
  Serial.print(" ppm");
  Serial.println();
  delay(1000);
}
