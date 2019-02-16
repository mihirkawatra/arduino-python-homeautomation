void setup() {
  pinMode(3,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
 Serial.begin(9600);
 digitalWrite(3,LOW);
  // put your setup code here, to run once:

}
void one()
{
  digitalWrite(3,HIGH);
}
void two()
{
  digitalWrite(3,HIGH);
  digitalWrite(5,HIGH);
  
}
void three()
{
  digitalWrite(3,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(5,HIGH);
  
}
void off()
{
  digitalWrite(3,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
  digitalWrite(7,LOW);
}
String r;
void loop() {
  while(Serial.available())
  {
   r=Serial.readString();
   Serial.println(r);
  }
  if(r=="fan_on")
  {
    digitalWrite(7,HIGH);
  }
  else if(r=="fan_off")
{
  digitalWrite(7,LOW);
}
  
  if(r=="on" || r=="three")
  {
    three();
  }
  else if(r=="two")
  {
    two();
  }
  else if(r=="one")
  {
    one();
  }
  else if(r=="all_on")
  {
    three();
    digitalWrite(7,HIGH);
  }
  else if(r=="off")
  {
    off();
  }
  
}
