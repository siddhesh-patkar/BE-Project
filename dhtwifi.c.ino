#include <FirebaseESP8266.h>
#include <ESP8266WiFi.h>
#include "DHTesp.h"


#define SSID "Redmi Note 10S"                                         //SSID 
#define PASSWORD "ASG#1512"                                           // Password

#define FIREBASE_HOST "dht-83e67-default-rtdb.firebaseio.com"         //Firebase Host ID
#define FIREBASE_AUTH "sKav0PzmvxDZCH96o8ZIgS6WGuroa4u5hU0hvYmM"      //Firebase Authentication Code

FirebaseData firebaseData;

DHTesp dht;

void setup()
{
  Serial.begin(115200);
  Serial.println();

  // connect to wifi.
  WiFi.begin(SSID, PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) 
  {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
 
  Serial.println("Status\tHumidity (%)\tTemperature (C)");
  dht.setup(16 , DHTesp::DHT22);                                 //Connect DHT sensor to GPIO 16
}

void loop()
{
  delay(2000);                                              
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();
  //Serial.print(dht.getStatusString());
  Serial.print("\t"); 
  Serial.print(humidity, 1);
  Serial.print("\t\t");
  Serial.println(temperature, 1);
  Firebase.setFloat(firebaseData,"Humidity",humidity);           //upload humidity to firebase
  Firebase.setFloat(firebaseData,"Temperature",temperature);     //upload temperature to firebase
}
