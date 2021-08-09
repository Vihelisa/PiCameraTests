/*#include <SoftwareSerial.h>

String x = "";
int pino_led = 13;
int y = 0;
long int t = 0,told = 0;
void setup() {
  Serial.begin(9600);
  pinMode(pino_led,OUTPUT);

}

void loop() {
  if(Serial.available()>0){ // confere se existe mensagens na porta serial
    x = Serial.readString(); // salva mensagem na variavel
    y = 100 - (x.toInt());
    Serial.println(y);
                    
         }
   t = millis();
   if( t -told > 5000){
   Serial.println(" Escreva um numero menor que 100");
   told = t;       
          //Serial.println(x); // escreve valor da variavel
  }


}
*/
