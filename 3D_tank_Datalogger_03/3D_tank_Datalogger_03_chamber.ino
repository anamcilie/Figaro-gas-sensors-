
// Figaro TGS 2611 to calculate Ro 
// DHT humidity/temperature sensors
// Written by Ana MC Ilie


#include "DHT.h"
  
#define DHTPINA A0   
#define DHTPINE A4  
#define DHTPINF A5  
   
#define DHTTYPEA DHT11  
#define DHTTYPEE DHT11   
#define DHTTYPEF DHT11  

// Initialize DHT sensor for normal 16mhz Arduino

DHT dhta(DHTPINA, DHTTYPEA);
DHT dhte(DHTPINE, DHTTYPEE);
DHT dhtf(DHTPINF, DHTTYPEF);

void setup() {

  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);

  Serial.begin(9600); 
  dhta.begin();
  dhte.begin();
  dhtf.begin();

Serial.println(",R0b,R0c,R0d,RSb,RSc,RSd,Vb,Vc,Vd,RHa,Ta,RHe,Te,RHf,Tf,Datalogger_03_chamber");


}
 
void loop() { 

 // digital pins for the Voltage heater VH 5 voltage

  digitalWrite(11, HIGH);   // sets the digital 11 ON
 
  digitalWrite(10, HIGH);   // sets the digital 10 ON
  
  digitalWrite(9, HIGH);   // sets the digital 9 ON


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
  
  
 // Wait a few seconds between measurements.
  delay(600);


  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds
  // Read temperature as Celsius 
  
  float ha = dhta.readHumidity();
  float ta = dhta.readTemperature();
  float he = dhte.readHumidity();
  float te = dhte.readTemperature();
  float hf = dhtf.readHumidity();
  float tf = dhtf.readTemperature();


  //print out the values                     

  
  Serial.print(",");                                
  Serial.print(R0b); 
  Serial.print(",");            
  Serial.print(R0c); 
  Serial.print(",");                      
  Serial.print(R0d);  
  Serial.print(",");                                   
  Serial.print(RS_airb); 
  Serial.print(",");                          
  Serial.print(RS_airc);
  Serial.print(",");                       
  Serial.print(RS_aird); 
  Serial.print(",");                             
  Serial.print(sensor_voltb); 
  Serial.print(",");                        
  Serial.print(sensor_voltc); 
  Serial.print(",");                       
  Serial.print(sensor_voltd); 
  Serial.print(",");  
  Serial.print(ha);
  Serial.print(","); 
  Serial.print(ta);
  Serial.print(","); 
  Serial.print(he);
  Serial.print(","); 
  Serial.print(te);
  Serial.print(",");
  Serial.print(hf);
  Serial.print(","); 
  Serial.print(tf);
  Serial.println(","); 

  delay(1000);                                  //Wait 1 second 
  
}
