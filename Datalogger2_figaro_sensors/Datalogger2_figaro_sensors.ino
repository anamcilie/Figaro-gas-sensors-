// code for the TGS2611-EOO_ana

//Gas Sensor Pin
#define g A0
#define h A1
#define i A2
#define j A3
#define k A4
#define l A5


void setup() 
{
Serial.begin(9600); // opens serial port, sets data rate 9600 bps

 pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);            // sets the digital pin 7 OUTPUT
  pinMode(6, OUTPUT);  

  
}

void loop() 
{
   // analog A0 in sensor g
  float VRL_g; 
 
  VRL_g = analogRead(A0)*(5.0/1023.0); 
 
  
  // analog A1 in sensor h
  float VRL_h; 

  VRL_h = analogRead(A1)*(5.0/1023.0); 
  

    // analog A2 in sensor i
 float VRL_i; 
 
  VRL_i = analogRead(A2)*(5.0/1023.0); 

  // analog A3 in sensor j
  float VRL_j; 
   
  VRL_j = analogRead(A3)*(5.0/1023.0); 


 // analog A4 in sensor k
  float VRL_k; 
   
  VRL_k = analogRead(A4)*(5.0/1023.0); 


// analog A5 in sensor l
  float VRL_l; 
  
  VRL_l = analogRead(A5)*(5.0/1023.0); 
 
   // digital pins for the Voltage heater VH 5 voltage

  digitalWrite(11, HIGH);   // sets the digital 11 ON
 
  digitalWrite(10, HIGH);   // sets the digital 10 ON
  
  digitalWrite(9, HIGH);   // sets the digital 9 ON
  
  digitalWrite(8, HIGH);   // sets the digital 8 ON

  digitalWrite(7, HIGH);   // sets the digital 7 ON
  
  digitalWrite(6, HIGH);   // sets the digital 6 ON
  
  
  

// print the data
    
   Serial.print("D1:  ");
  Serial.print("      ");
  
  Serial.print(VRL_g); 
  Serial.print("     ");
  
  Serial.print(VRL_h); 
  Serial.print("     ");
  
  Serial.print(VRL_i); 
  Serial.print("    ");  
  
  Serial.print(VRL_j); 
  Serial.print("    ");
  
  Serial.print(VRL_k); 
  Serial.print("    "); 
  
  Serial.println(VRL_l); 
 
 
  delay(1000);   // 1 sec
  

}
