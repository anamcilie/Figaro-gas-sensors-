// DHT humidity/temperature sensors
// Written by Ana MC Ilie

#include "DHT.h"

#define DHTPINA A0   
#define DHTPINB A1  
#define DHTPINC A2  
#define DHTPIND A3  
#define DHTPINE A4  
#define DHTPINF A5  
  
#define DHTTYPEA DHT11  
#define DHTTYPEB DHT11  
#define DHTTYPEC DHT11  
#define DHTTYPED DHT11  
#define DHTTYPEE DHT11  
#define DHTTYPEF DHT11  

// Initialize DHT sensor for normal 16mhz Arduino
DHT dhta(DHTPINA, DHTTYPEA);
DHT dhtb(DHTPINB, DHTTYPEB);
DHT dhtc(DHTPINC, DHTTYPEC);
DHT dhtd(DHTPIND, DHTTYPED);
DHT dhte(DHTPINE, DHTTYPEE);
DHT dhtf(DHTPINF, DHTTYPEF);


void setup() {
  Serial.begin(9600); 

dhta.begin();
dhtb.begin();
dhtc.begin();
dhtd.begin();
dhte.begin();
dhtf.begin();

Serial.println(",RHa,Ta,RHb,Tb,RHc,Tc,RHd,Td,RHe,Te,RHf,Tf");
  
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);


  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds
  // Read temperature as Celsius 
  
  float ha = dhta.readHumidity();
  float ta = dhta.readTemperature();


  float hb = dhtb.readHumidity();
  float tb = dhtb.readTemperature();


  float hc = dhtc.readHumidity();
  float tc = dhtc.readTemperature();


  float hd = dhtd.readHumidity();
  float td = dhtd.readTemperature();

  float he = dhte.readHumidity();
  float te = dhte.readTemperature();

  float hf = dhtf.readHumidity();
  float tf = dhtf.readTemperature();


// Print out the values

  Serial.print(","); 
  Serial.print(ha);
  Serial.print(","); 
  Serial.print(ta);
  Serial.print(","); 
 
  
  Serial.print(hb);
  Serial.print(","); 
  Serial.print(tb);
  Serial.print(","); 


  Serial.print(hc);
  Serial.print(","); 
  Serial.print(tc);
  Serial.print(","); 



  Serial.print(hd);
  Serial.print(","); 
  Serial.print(td);
  Serial.print(","); 


 
  Serial.print(he);
  Serial.print(","); 
  Serial.print(te);
  Serial.print(","); 



  Serial.print(hf);
  Serial.print(","); 
  Serial.println(tf);


}
