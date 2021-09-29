// code for the TGS2611-EOO_ana

//Gas Sensor Pin
#define a A0
#define b A1
#define c A2
#define d A3
#define e A4
#define f A5


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
   // analog A0 in sensor a
  float VRL_a; 
 
  VRL_a = analogRead(A0)*(5.0/1023.0); 

  
  // analog A1 in sensor b
  float VRL_b; 
   
  VRL_b = analogRead(A1)*(5.0/1023.0); 
 

    // analog A2 in sensor c
 float VRL_c; 
   
  VRL_c = analogRead(A2)*(5.0/1023.0); 


  // analog A3 in sensor d
  float VRL_d; 
   
  VRL_d = analogRead(A3)*(5.0/1023.0); 
 

 // analog A4 in sensor e
  float VRL_e; 
 
  VRL_e = analogRead(A4)*(5.0/1023.0); 


// analog A5 in sensor f
  float VRL_f; 

   
  VRL_f = analogRead(A5)*(5.0/1023.0); 
 


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
  
  Serial.print(VRL_a); 
  Serial.print("     ");
  
  Serial.print(VRL_b); 
  Serial.print("     ");
  
  Serial.print(VRL_c); 
  Serial.print("    ");  
  
  Serial.print(VRL_d); 
  Serial.print("    ");
  
  Serial.print(VRL_e); 
  Serial.print("    "); 
  
  Serial.println(VRL_f); 
 
 
  delay(1000);   // 1 sec
  

}
