#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include <Servo.h>

#define FIREBASE_HOST "smartdoorgp.firebaseio.com"
#define FIREBASE_AUTH "xWdXdam02D7Tkxgkbi55iiHQta73ecc0HKaqnD67"

const char* ssid = "MM";
const char* password = "nopassword";

//const int trigPin = D6;
//const int echoPin = D7;
int state=0, pos;
long duration;
int distance;
String Door,Face;
Servo myservo;


void setup() {
  Serial.begin(9600);
  //off();
  Serial.println("Connecting");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("Connection Failed! Rebooting...");
    delay(5000);
    ESP.restart();
  }
  Serial.println("Connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  //pinMode(trigPin, OUTPUT);
  //pinMode(echoPin, INPUT);
  myservo.attach(D1);
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {
  //verification();
  Door = Firebase.getString("SmartDoor/Door");
  Face = Firebase.getString("SmartDoor/Face");
  
  if(Door=="\"Open\"" && state==1){
    Open();
    Door="";
    Firebase.setString("SmartDoor/Door", "");
  }
  if(Door=="\"Close\"" && state==0){
    Close();
    Door="";
    Firebase.setString("SmartDoor/Door", "");
  }
  if(Face=="mm" && state==1){
    Open();
    delay(5000);
    Close();
    Face="";
    Firebase.setString("SmartDoor/Face", "");
  }
  }

/*  void off(){
  digitalWrite(trigPin,LOW);
  digitalWrite(echoPin,LOW);
}


void verification(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  Serial.print("Wall Distance: ");
  Serial.println(distance);

  if(distance<=2){
    //Already Open
    state=0;
    Firebase.setString("SmartDoor/State", "Door is Open");
    
  }
  else{
    //Closed
    state=1;
    Firebase.setString("SmartDoor/State", "Door is Close");
  }
}*/

void Open(){
  for (pos = 50; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    Serial.println(pos);
  }
  state=0;
  Firebase.setString("SmartDoor/State", "Door is Open");
}
void Close(){
  for (pos = 180; pos >= 50; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    Serial.println(pos);
  }
  state=1;
  Firebase.setString("SmartDoor/State", "Door is Close");
}
