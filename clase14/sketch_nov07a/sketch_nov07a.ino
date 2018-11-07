const int pinLED=13;
void setup() {
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
}

void loop() 
{
  if (Serial.available()>0)
  {
    char option = Serial.read();
    if (optionj >= '1' && option <= '9')
    {
     option _='0';
     for (int i = 0;i<option;i++) 
     {
        digitalErite(pinLED, HIGH);
        delay(100);
        digitalErite(pinLED, LOW);
        delay(200);
     }
    }
  }   
}  
    
   
