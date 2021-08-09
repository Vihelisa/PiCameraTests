//Importações:
#include <SoftwareSerial.h>

//Variáveis:
int led = 13;
char dado;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    dado = Serial.read();
    Serial.println(dado);
    if (dado == '1') {
      digitalWrite(led, HIGH);
      Serial.println("LED Ligado!!");
    }
    else if (dado == '0') {
      digitalWrite(led, LOW);
      Serial.println("LED Desligado!");
    }
  }
}
