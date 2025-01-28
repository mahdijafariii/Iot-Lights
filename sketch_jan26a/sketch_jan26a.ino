#include <ESP8266WiFi.h>

const char* ssid = "ESP8266-Access-Point";
const char* password = "123456789";

WiFiServer server(8888);
const int ledPin = LED_BUILTIN;

void setup() {
  Serial.begin(115200);
  delay(10);

  pinMode(ledPin, OUTPUT);

  Serial.println("Setting up Access Point...");
  WiFi.softAP(ssid, password);
  server.begin();

  Serial.println("Server started");
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());
}
void loop() {

  int numConnected = WiFi.softAPgetStationNum();
  WiFiClient client = server.available();

  String telegramRes = "";
  String clientData = "";



  if (client) {
    Serial.println("New Client Connected");
    while (client.connected()) {
      while (client.available()) {

        char c = client.read();
        clientData += c;
      }
      if (clientData.length() > 0) {
        Serial.print(clientData);
        delay(3000);
        String clientRes = Serial.readString();
        String stringResult = clientRes;
        if (stringResult == "A") {
          digitalWrite(ledPin, LOW);
          client.println("room number 1 turn on");
        }
        if (stringResult == "B") {
          digitalWrite(ledPin, HIGH);
          client.println("room number 1 turn off");
        }
        if (stringResult == "C") {
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          client.println("room number 2 turn on");
        }
        if (stringResult == "D") {
          digitalWrite(ledPin, HIGH);
          client.println("room number 2 turn off");
        }
        if (stringResult == "E") {
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          client.println("room number 1 turn on and room number 2 turn off ");
        }
        if (stringResult == "F") {
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);
          digitalWrite(ledPin, HIGH);
          delay(500);
          digitalWrite(ledPin, LOW);
          delay(500);

          client.println("room number 2 turn on and room number 1 turn off ");
        }
        client.println("Message received:");
        client.println(clientData);

        break;
      }
    }
  } else {
    telegramRes = Serial.readString();
    if (telegramRes.length() > 0) {
      delay(3000);
      String stringResult = telegramRes;
      if (stringResult == "A") {
        digitalWrite(ledPin, LOW);
      }
      if (stringResult == "B") {
        digitalWrite(ledPin, HIGH);
      }
      if (stringResult == "C") {
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
      }
      if (stringResult == "D") {
        digitalWrite(ledPin, HIGH);
      }
      if (stringResult == "E") {
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
      }
      if (stringResult == "F") {
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
      }
    }
  }

  delay(100);
}
