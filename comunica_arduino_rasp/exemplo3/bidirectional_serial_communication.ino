//Variaveis:
String data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
// Quando entra uma informação na serial, o rasp printa a mensagem.
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);
    }
}
