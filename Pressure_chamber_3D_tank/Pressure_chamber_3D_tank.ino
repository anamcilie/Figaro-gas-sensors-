
// Figaro TGS 2611 to calculate Ro 
// Written by Ana MC Ilie
#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <SPI.h>

Adafruit_BMP085 bmp;

void setup() {
Serial.begin(9600);
  if (!bmp.begin()) {
  Serial.println("Could not find a valid BMP085 sensor, check wiring!");
  while (1) {}
  }
  
  Serial.begin(9600);
  pinMode(11, OUTPUT);


Serial.println(",R0b,RSb,Vb,T*C,Pressure_Pa,Altitude_meters,Pa_sealevel, Datalogger_chamber");


}
 
void loop() { 

 // digital pins for the Voltage heater VH 5 voltage
  
  digitalWrite(11, HIGH);   // sets the digital 11 ON


// read Ro for a analog A1

   float sensor_voltb;               //Define variable for sensor voltage 
  float RS_airb;                    //Define variable for sensor resistance
  float R0b;                       //Define variable for R0
  float sensorValueb;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValueb = sensorValueb + analogRead(A1); //Add analog values of sensor 500 times 
  }
  sensorValueb = sensorValueb/500.0;              //Take average of readings
  sensor_voltb = analogRead(A1)*(5.0/1023.0);       //Convert average to voltage 
  
  RS_airb = ((5.0*10)/sensor_voltb)-10;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_airb = ((5.0-sensor_voltb)/sensor_voltb);       //Calculate RS in fresh air omit the Rl
  R0b = RS_airb/14.51;   

 // Wait a few seconds between measurements.
  delay(600);

  
  //print out the values                     

  
  Serial.print(",");                                
  Serial.print(R0b); 
  Serial.print(",");                                          
  Serial.print(RS_airb); 
  Serial.print(",");                                               
  Serial.print(sensor_voltb); 
  Serial.print(",");                        
  Serial.print(bmp.readTemperature()); 
  Serial.print(",");   
  Serial.print(bmp.readPressure()); 
  Serial.print(",");                    
  Serial.print(bmp.readAltitude()); 
  Serial.print(","); 
  Serial.print(bmp.readSealevelPressure());
  Serial.println(","); 
  
  delay(1000);                                  //Wait 1 second 
  
}
