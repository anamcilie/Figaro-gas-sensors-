// code for the TGS2611-EOO to obtain the methane concentrations in ppm_ana

//Gas Sensor Pin

#define b A1
#define c A2
#define d A3
#define e A4
#define f A5


//Gas Sensor Load Resistance (RL)

#define RL_b 4.75
#define RL_c 4.75
#define RL_d 4.75
#define RL_e 4.75
#define RL_f 4.75



float CH4_bA = -0.81361;
float CH4_bB = -0.007925;

float CH4_cA = -0.81361;
float CH4_cB = -0.007925;

float CH4_dA = -0.81361;
float CH4_dB = -0.007925;

float CH4_eA = -0.81361;
float CH4_eB = -0.007925;

float CH4_fA = -0.81361;
float CH4_fB = -0.007925;


void setup() 
{
Serial.begin(9600); // opens serial port, sets data rate 9600 bps
}

void loop() 
{


// read the sensor b in analog A1

  float VRL_b; 
  float Rs_b; 
  float Ro_b = -0.03;
  float ratio_b;
   
  VRL_b = analogRead(b)*(5.0/1023.0); 
  Rs_b = ((5.0/VRL_b)-1)*(RL_b);
  ratio_b = Rs_b/Ro_b;
  
  float ppm_CH4b = CH4_bA * pow(ratio_b, CH4_bB);
    
// read the sensor c in analog A2

  float VRL_c; 
  float Rs_c; 
  float Ro_c = -0.03;
  float ratio_c;
   
  VRL_c = analogRead(c)*(5.0/1023.0); 
  Rs_c = ((5.0/VRL_c)-1)*(RL_c);
  ratio_c = Rs_c/Ro_c;
  
  float ppm_CH4c = CH4_cA * pow(ratio_c, CH4_cB);



  // read the sensor d in analog A3

  float VRL_d; 
  float Rs_d; 
  float Ro_d = -0.03;
  float ratio_d;
   
  VRL_d = analogRead(d)*(5.0/1023.0); 
  Rs_d = ((5.0/VRL_d)-1)*(RL_d);
  ratio_d = Rs_d/Ro_d;
  
  float ppm_CH4d = CH4_dA * pow(ratio_d, CH4_dB);


  // read the sensor e in analog A4

  float VRL_e; 
  float Rs_e; 
  float Ro_e = -0.03;
  float ratio_e;
   
  VRL_e = analogRead(e)*(5.0/1023.0); 
  Rs_e = ((5.0/VRL_e)-1)*(RL_e);
  ratio_e = Rs_e/Ro_e;
  
  float ppm_CH4e = CH4_eA * pow(ratio_e, CH4_eB);



// read the sensor f in analog A5

  float VRL_f; 
  float Rs_f; 
  float Ro_f = -0.03;
  float ratio_f;
   
  VRL_f = analogRead(f)*(5.0/1023.0); 
  Rs_f = ((5.0/VRL_f)-1)*(RL_f);
  ratio_f = Rs_f/Ro_f;
  
  float ppm_CH4f = CH4_fA * pow(ratio_f, CH4_fB);

  

// print the output of methane, all sensors 


  Serial.print("CH4_b =  "); 
  Serial.print(ppm_CH4b); 
  Serial.print(", "); 


  Serial.print("CH4_c =  "); 
  Serial.print(ppm_CH4c); 
  Serial.print(", "); 

   Serial.print("CH4_d =  "); 
  Serial.print(ppm_CH4d); 
  Serial.print(", "); 


   Serial.print("CH4_e =  "); 
    Serial.print(ppm_CH4e); 
    Serial.print(", "); 

   Serial.print("CH4_f =  "); 
    Serial.println(ppm_CH4f); 
 


delay(3000);   // 3 sec

}
