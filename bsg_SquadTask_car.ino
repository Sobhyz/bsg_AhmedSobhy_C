int motors[3][4]={{3,4,5},{6,7,8}};
#include "SoftwareSerial.h"
char f='s';

SoftwareSerial node(0,1);

void setup() {
  for(int i=0;i<2;i++){
    for(int j=0;j<3;j++){
        pinMode(motors[i][j],OUTPUT);
    }
  }
  Serial.begin(9600);
  node.begin(9600);
}


void loop() {
  if(node.available())
  {
    f = node.read();
  }
  Serial.println(f);
  if(f == 'a')
  {
    digitalWrite(motors[0][0], HIGH);
    digitalWrite(motors[1][0], HIGH);
    digitalWrite(motors[0][1], HIGH);
    digitalWrite(motors[0][2], LOW);
    digitalWrite(motors[1][1], HIGH);
    digitalWrite(motors[1][2], LOW);
    delay(100);
  }
  else{
    digitalWrite(motors[0][0], LOW);
    digitalWrite(motors[1][0], LOW);
    delay(100);
  }
  if(f == 'b')
  {
    digitalWrite(motors[0][0], HIGH);
    digitalWrite(motors[1][0], HIGH);
    digitalWrite(motors[0][2], HIGH);
    digitalWrite(motors[0][1], LOW);
    digitalWrite(motors[1][2], HIGH);
    digitalWrite(motors[1][1], LOW);
    delay(100);
  }
  else{
    digitalWrite(motors[0][0], LOW);
    digitalWrite(motors[1][0], LOW);
    delay(100);
  }
  if(f == 'r')
  {
    digitalWrite(motors[1][0], HIGH);
    digitalWrite(motors[1][1], HIGH);
    digitalWrite(motors[1][2], LOW);
    delay(100);
  }
  else{
    digitalWrite(motors[1][0], LOW);
    delay(100);
  }
  if(f == 'l')
  {
    digitalWrite(motors[0][0], HIGH);
    digitalWrite(motors[0][2], HIGH);
    digitalWrite(motors[0][1], LOW);
    delay(100);
  }
  else{
    digitalWrite(motors[0][0], LOW);
    delay(100);
  }
}
