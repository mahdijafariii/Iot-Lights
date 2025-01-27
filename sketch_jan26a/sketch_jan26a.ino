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
  if (client) {
    Serial.println("New Client Connected");

    String clientData = ""; 
    while (client.connected()) {
      while (client.available()) {
        char c = client.read(); 
        clientData += c;
      }

      if (clientData.length() > 0) {
        Serial.print(clientData);
        delay(1000);
        String stringData = Serial.readString();
        if (stringData == "A") {
          digitalWrite(ledPin, LOW);
        }
        if (stringData == "B") {
          digitalWrite(ledPin, HIGH);
        }
        if (stringData == "C") {
            digitalWrite(ledPin, HIGH);
            delay(500);
              digitalWrite(ledPin, LOW);
            delay(500);
        }
        if (stringData == "D") {
          digitalWrite(ledPin, HIGH);
        }
        // ارسال پاسخ به کلاینت
        client.print("Message received:");
        client.print(clientData);

        break;  
      }
    }
  }

  delay(100);  
}
