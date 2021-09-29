// code for the TGS2611-EOO_ana

#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

//Gas Sensor Pin
#define m A0
#define n A1
#define o A2



void setup() 
{
Serial.begin(9600); // opens serial port, sets data rate 9600 bps

 pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);

Serial.begin(9600);
  if (!bmp.begin()) {
  Serial.println("Could not find a valid BMP085 sensor, check wiring!");
  while (1) {}
  }

  
}

void loop() 
{
   // analog A0 in sensor m
  float VRL_m; 
   
  VRL_m = analogRead(A0)*(5.0/1023.0); 

  
  // analog A1 in sensor n
  float VRL_n; 
 
  VRL_n = analogRead(A1)*(5.0/1023.0); 
  

    // analog A2 in sensor o
 float VRL_o; 
   
  VRL_o = analogRead(A2)*(5.0/1023.0); 
  

   // digital pins for the Voltage heater VH 5 voltage

  digitalWrite(11, HIGH);   // sets the digital 11 ON
 
  digitalWrite(10, HIGH);   // sets the digital 10 ON
  
  digitalWrite(9, HIGH);   // sets the digital 9 ON
 
  
  

// print the data
    
   Serial.print("D3:  ");
  Serial.print("      ");
  
  Serial.print(VRL_m); 
  Serial.print("     ");
  
  Serial.print(VRL_n); 
  Serial.print("     ");
  
  Serial.print(VRL_o); 
  Serial.print("    ");  

  Serial.print("T*C: ");
  Serial.print(bmp.readTemperature());
  Serial.print("    "); 
    
  Serial.print("Pascal: ");
  Serial.println(bmp.readPressure());
  
 
 
  delay(1000);   // 1 sec
  

}
