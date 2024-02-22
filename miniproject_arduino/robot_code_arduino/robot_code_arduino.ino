#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/Float32.h>

#define potPin A5
#define encoderPinA 2
#define encoderPinB 3
#define clearButton 8

ros::NodeHandle  nh;
std_msgs::Int16 encoderData;
std_msgs::Int16 potenData;



const int stepPin = 3; 
const int dirPin = 2; 

const int numReadings = 10; 
int readings[numReadings]; 
int index = 0; 
int total = 0; 
ros::Publisher Encodepub("Topic_Feedback_encode", &encoderData );
ros::Publisher Potenpub("Topic_Feedback_poten", &potenData );


void GuiXcontrol(const std_msgs::Float32& cmd_msgX)
{
  int valueX = cmd_msgX.data;
  
}

void GuiYcontrol(const std_msgs::Float32& cmd_msgY)
{
  int valueY = cmd_msgY.data;
}

ros::Subscriber<std_msgs::Float32> GuiXsub("Topic_DataXFrom_Gui", &GuiXcontrol);
ros::Subscriber<std_msgs::Float32> GuiYsub("Topic_DataYFrom_Gui", &GuiYcontrol);


volatile unsigned int encoderPos = 0;  
unsigned int lastReportedPos = 1;   
static boolean rotating = false;    

boolean A_set = false;
boolean B_set = false;
int sum=0;
int average =0;
void setup() 
{ 
   pinMode(encoderPinA, INPUT_PULLUP); 
   pinMode(encoderPinB, INPUT_PULLUP);
   pinMode(clearButton, INPUT_PULLUP);
   attachInterrupt(0, doEncoderA, CHANGE); 
   attachInterrupt(1, doEncoderB, CHANGE); 
   pinMode(stepPin,OUTPUT); 
   pinMode(dirPin,OUTPUT);
   nh.initNode();
   nh.advertise(Encodepub);  
   nh.advertise(Potenpub);

   nh.subscribe(GuiXsub);
   nh.subscribe(GuiYsub);

 } 

void loop() { 
  total = total - readings[index]; 
  readings[index] = analogRead(potPin); 
  total = total + readings[index]; 
  index = (index + 1) % numReadings; 
  average = total / numReadings; 
  average = average/10;
if(sum != average)
{
  float X=0;
  if(average<17)
  {
    X=3;
  }
  else if(average<17+17)
  {
    X=2;
  }
  else if(average<17+17+17)
  {
    X=1;
  }
  else if(average<17+17+17+17)
  {
    X=0;
  }
   else if(average<17+17+17+17+17)
  {
    X=-1;
  }
   else if(average<17+17+17+17+17+17)
  {
    X=-2;
  }
  else if(average<17+17+17+17+17+17+17)
  {
    X=-3;
  }
  else
  {
    X=-3;
  }
  potenData.data = X;
  Potenpub.publish(&potenData);
  sum = average;
}
rotating = true;  // reset the debouncer
  if (lastReportedPos != encoderPos) {
          if(encoderPos==65535)
    {
      encoderPos = 0;
      }
       if(encoderPos>13)
    {
      encoderPos = 14;
      }
    float Y=0;
      if(encoderPos<2)
  {
    Y=3;
  }
  else if(encoderPos<4)
  {
    Y=2;
  }
  else if(encoderPos<6)
  {
    Y=1;
  }
  else if(encoderPos<8)
  {
    Y=0;
  }
   else if(encoderPos<10)
  {
    Y=-1;
  }
   else if(encoderPos<12)
  {
    Y=-2;
  }
  else if(encoderPos<14)
  {
    Y=-3;
  }
  else
  {
    Y=-3;
  }
    
    encoderData.data = Y;
    Encodepub.publish(&encoderData);
 
    lastReportedPos = encoderPos;
  }
  if (digitalRead(clearButton) == LOW )  {
    encoderPos = 0;
    delay(200);
  }

  nh.spinOnce();
  delay(1);
 }

 
void doEncoderA() {
  // debounce
  if ( rotating ) delay (1);  
  
  if ( digitalRead(encoderPinA) != A_set ) { 
    A_set = !A_set;
    if ( A_set && !B_set )
      encoderPos += 1;
    rotating = false;  
  }
}

void doEncoderB() {
  if ( rotating ) delay (1);
  if ( digitalRead(encoderPinB) != B_set ) {
    B_set = !B_set;
    if ( B_set && !A_set )
      encoderPos -= 1;
    rotating = false;
  }
}
