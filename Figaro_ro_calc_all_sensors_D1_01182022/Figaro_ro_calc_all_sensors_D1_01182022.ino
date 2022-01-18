
// Figaro TGS 2611 to calculate Ro, sketch_ana

#include <Wire.h>

#include <SPI.h>


void setup() {


  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);            // sets the digital pin 7 OUTPUT 

  Serial.println(",R0b,R0c,R0d,R0e,R0f,RSb,RSc,RSd,RSe,RSf,Vb,Vc,Vd,Ve,Vf, Datalogger_1");
  
}
 
void loop() { 

// read Ro for b analog A1

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

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0b = RS_airb/14.51;   


// read Ro for sensor c in analog A2

   float sensor_voltc;               //Define variable for sensor voltage 
  float RS_airc;                    //Define variable for sensor resistance
  float R0c;                       //Define variable for R0
  float sensorValuec;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValuec = sensorValuec + analogRead(A2); //Add analog values of sensor 500 times 
  }
  sensorValuec = sensorValuec/500.0;              //Take average of readings
  sensor_voltc = analogRead(A2)*(5.0/1023.0);       //Convert average to voltage 
  
  RS_airc = ((5.0*10)/sensor_voltc)-10;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0c = RS_airc/14.51;   


  // read Ro for sensor d in analog A3

   float sensor_voltd;               //Define variable for sensor voltage 
  float RS_aird;                    //Define variable for sensor resistance
  float R0d;                       //Define variable for R0
  float sensorValued;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValued = sensorValued + analogRead(A3); //Add analog values of sensor 500 times 
  }
  sensorValued = sensorValued/500.0;              //Take average of readings
  sensor_voltd = analogRead(A3)*(5.0/1023.0);       //Convert average to voltage 
  
  RS_aird = ((5.0*10)/sensor_voltd)-10;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0d = RS_aird/14.51; 


  // read Ro for sensor e in analog A4

   float sensor_volte;               //Define variable for sensor voltage 
  float RS_aire;                    //Define variable for sensor resistance
  float R0e;                       //Define variable for R0
 float sensorValuee;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValuee = sensorValuee + analogRead(A4); //Add analog values of sensor 500 times 
  }
  sensorValuee = sensorValuee/500.0;              //Take average of readings
  sensor_volte = analogRead(A4)*(5.0/1023.0);       //Convert average to voltage 
  
  RS_aire = ((5.0*10)/sensor_volte)-10;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0e = RS_aire/14.51;   



  
  // read Ro for sensor f in analog A5

   float sensor_voltf;               //Define variable for sensor voltage 
  float RS_airf;                    //Define variable for sensor resistance
  float R0f;                       //Define variable for R0
  float sensorValuef;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValuef = sensorValuef + analogRead(A5); //Add analog values of sensor 500 times 
  }
  sensorValuef = sensorValuef/500.0;              //Take average of readings
  sensor_voltf = analogRead(A5)*(5.0/1023.0);       //Convert average to voltage 
  
  RS_airf = ((5.0*10)/sensor_voltf)-10;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0f = RS_airf/14.51; 

  
  
  // digital pins for the Voltage heater VH 5 voltage
 
  digitalWrite(10, HIGH);   // sets the digital 10 ON
  
  digitalWrite(9, HIGH);   // sets the digital 9 ON
  
  digitalWrite(8, HIGH);   // sets the digital 8 ON

  digitalWrite(7, HIGH);   // sets the digital 7 ON

  digitalWrite(6, HIGH);
  
  //print out the values                     
                      
  Serial.print(R0b); 
  Serial.print(",");
                     
  Serial.print(R0c);   
  Serial.print(",");
                   
  Serial.print(R0d);
  Serial.print(","); 
                         
  Serial.print(R0e);  
  Serial.print(","); 
                      
  Serial.print(R0f);
  Serial.print(",");
                         
                     
  Serial.print(RS_airb); 
  Serial.print(",");  
                      
  Serial.print(RS_airc); 
  Serial.print(","); 
                       
  Serial.print(RS_aird); 
  Serial.print(",");  
                       
  Serial.print(RS_aire); 
  Serial.print(",");    
                      
  Serial.print(RS_airf); 
  Serial.print(",");
                        
                      
  Serial.print(sensor_voltb); 
  Serial.print(",");
                      
  Serial.print(sensor_voltc); 
  Serial.print(",");
                         
  Serial.print(sensor_voltd); 
  Serial.print(",");
                      
  Serial.print(sensor_volte); 
  Serial.print(",");
                        
  Serial.println(sensor_voltf); 
 
    
  delay(1000);                                  //Wait 1 second 
  
}
