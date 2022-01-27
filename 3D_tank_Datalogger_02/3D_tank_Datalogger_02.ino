
// Figaro TGS 2611 to calculate Ro 
// DHT humidity/temperature sensors
// Written by Ana MC Ilie


#include "DHT.h"
  
#define DHTPINB A1   
#define DHTPIND A3  
#define DHTPINF A5  
   
#define DHTTYPEB DHT11  
#define DHTTYPED DHT11   
#define DHTTYPEF DHT11  

// Initialize DHT sensor for normal 16mhz Arduino

DHT dhtb(DHTPINB, DHTTYPEB);
DHT dhtd(DHTPIND, DHTTYPED);
DHT dhtf(DHTPINF, DHTTYPEF);

void setup() {

  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);

  Serial.begin(9600); 
  dhtb.begin();
  dhtd.begin();
  dhtf.begin();

Serial.println(",R0a,R0c,R0e,RSa,RSc,RSe,RSf,Va,Vc,Ve,RHb,Tb,RHd,Td,RHf,Tf,Datalogger_2");


}
 
void loop() { 

 // digital pins for the Voltage heater VH 5 voltage

  digitalWrite(11, HIGH);   // sets the digital 11 ON
 
  digitalWrite(10, HIGH);   // sets the digital 10 ON
  
  digitalWrite(9, HIGH);   // sets the digital 9 ON


// read Ro for a analog A0

   float sensor_volta;               //Define variable for sensor voltage 
  float RS_aira;                    //Define variable for sensor resistance
  float R0a;                       //Define variable for R0
  float sensorValuea;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValuea = sensorValuea + analogRead(A0); //Add analog values of sensor 500 times 
  }
  sensorValuea = sensorValuea/500.0;              //Take average of readings
  sensor_volta = analogRead(A0)*(5.0/1023.0);       //Convert average to voltage 
  
  RS_aira = ((5.0*10)/sensor_volta)-10;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0a = RS_aira/14.51;   


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
  
  
 // Wait a few seconds between measurements.
  delay(600);


  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds
  // Read temperature as Celsius 
  
  float hb = dhtb.readHumidity();
  float tb = dhtb.readTemperature();
  float hd = dhtd.readHumidity();
  float td = dhtd.readTemperature();
  float hf = dhtf.readHumidity();
  float tf = dhtf.readTemperature();


  //print out the values                     

  
  Serial.print(",");                                
  Serial.print(R0a); 
  Serial.print(",");            
  Serial.print(R0c); 
  Serial.print(",");                      
  Serial.print(R0e);  
  Serial.print(",");                                   
  Serial.print(RS_aira); 
  Serial.print(",");                          
  Serial.print(RS_airc);
  Serial.print(",");                       
  Serial.print(RS_aire); 
  Serial.print(",");                             
  Serial.print(sensor_volta); 
  Serial.print(",");                        
  Serial.print(sensor_voltc); 
  Serial.print(",");                       
  Serial.print(sensor_volte); 
  Serial.print(",");  
  Serial.print(hb);
  Serial.print(","); 
  Serial.print(tb);
  Serial.print(","); 
  Serial.print(hd);
  Serial.print(","); 
  Serial.print(td);
  Serial.print(",");
  Serial.print(hf);
  Serial.print(","); 
  Serial.print(tf);
  Serial.println(","); 

  delay(1000);                                  //Wait 1 second 
  
}
