
// Figaro TGS 2611 to calculate Ro for the 4 gas sensors, sketch_ana

void setup() {
  Serial.begin(9600); //Baud rate 
}
 
void loop() { 


// read Ro for sensor b in analog A1

   float sensor_voltb;               //Define variable for sensor voltage 
  float RS_airb;                    //Define variable for sensor resistance
  float R0b;                       //Define variable for R0
  float sensorValueb;              //Define variable for analog readings 
  for(int x = 0 ; x < 500 ; x++)  //Start for loop 
  {
    sensorValueb = sensorValueb + analogRead(A1); //Add analog values of sensor 500 times 
  }
  sensorValueb = sensorValueb/500.0;              //Take average of readings
  sensor_voltb = sensorValueb*(5.0/1023.0);       //Convert average to voltage 
  
  RS_airb = ((5.0*0.45)/sensor_voltb)-0.45;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

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
  sensor_voltc = sensorValuec*(5.0/1023.0);       //Convert average to voltage 
  
  RS_airc = ((5.0*0.45)/sensor_voltc)-0.45;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

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
  sensor_voltd = sensorValued*(5.0/1023.0);       //Convert average to voltage 
  
  RS_aird = ((5.0*0.45)/sensor_voltd)-0.45;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

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
  sensor_volte = sensorValuee*(5.0/1023.0);       //Convert average to voltage 
  
  RS_aire = ((5.0*0.45)/sensor_volte)-0.45;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

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
  sensor_voltf = sensorValuef*(5.0/1023.0);       //Convert average to voltage 
  
  RS_airf = ((5.0*0.45)/sensor_voltf)-0.45;       //Calculate RS in fresh air Rs = ((Vc * Rl)/sensorVolt))-Rl

  // RS_air = ((5.0-sensor_volt)/sensor_volt);       //Calculate RS in fresh air omit the Rl
  R0f = RS_airf/14.51; 
  
  
  //Calculate R0                      

   Serial.print("R0b = ");                        
  Serial.print(R0b); 
  Serial.print(", ");                              

   Serial.print("R0c = ");                       
  Serial.print(R0c);   
  Serial.print(", ");                            

   Serial.print("R0d = ");                        
  Serial.print(R0d);
  Serial.print(", ");                              

     Serial.print("R0e = ");                        
  Serial.print(R0e);  
  Serial.print(", ");                            

   Serial.print("R0f = ");                        
  Serial.println(R0f);
                           
  delay(3000);                                  //Wait 1 second 
}
