#include <ESP8266WiFi.h>

const char* ssid = "your wifi ssid"; 
const char* password = "your wifi password"; 

WiFiServer server(80);

// Define motor control pins
const int motorForwardPin = D1;   // Pin for moving forward
const int motorBackwardPin = D2;  // Pin for moving backward
const int motorLeftPin = D3;      // Pin for turning left
const int motorRightPin = D4;     // Pin for turning right

void setup() {
  // Set motor pins as outputs
  pinMode(motorForwardPin, OUTPUT);
  pinMode(motorBackwardPin, OUTPUT);
  pinMode(motorLeftPin, OUTPUT);
  pinMode(motorRightPin, OUTPUT);

  Serial.begin(115200); // Start serial communication for debugging

  WiFi.mode(WIFI_STA); 
  WiFi.begin(ssid, password); 
  while (WiFi.status() != WL_CONNECTED) { 
    delay(500); 
    Serial.print("."); // Print dots while connecting
  } 

  server.begin(); 
  Serial.println("Server started");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP()); // Print the IP address
}

void loop() {
  WiFiClient client = server.available(); 

  if (client) { // Check if a client is connected
    String request = client.readStringUntil('n'); 
    client.flush(); 

    if (request.indexOf("/Forward") != -1) {
      moveForward();
    } else if (request.indexOf("/Backward") != -1) {
      moveBackward();
    } else if (request.indexOf("/Left") != -1) {
      turnLeft();
    } else if (request.indexOf("/Right") != -1) {
      turnRight();
    } else if (request.indexOf("/Stop") != -1) {
      stopMotors();
    }

    // Send a response back to the client
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/plain");
    client.println("Connection: close");
    client.println();
    client.println("Command received");
    
    client.stop(); // Close the connection
  }
}

void turnRight() {
  digitalWrite(motorForwardPin, HIGH);
  digitalWrite(motorBackwardPin, LOW);
  digitalWrite(motorLeftPin, HIGH);
  digitalWrite(motorRightPin, LOW);
}

void turnLeft() {
  digitalWrite(motorForwardPin, LOW);
  digitalWrite(motorBackwardPin, HIGH);
  digitalWrite(motorLeftPin, LOW);
  digitalWrite(motorRightPin, HIGH);
}

void moveBackward() {
  digitalWrite(motorForwardPin, LOW);
  digitalWrite(motorBackwardPin, HIGH);
  digitalWrite(motorLeftPin, HIGH);
  digitalWrite(motorRightPin, LOW);
}

void moveForward() {
  digitalWrite(motorForwardPin, HIGH);
  digitalWrite(motorBackwardPin, LOW);
  digitalWrite(motorLeftPin, LOW);
  digitalWrite(motorRightPin, HIGH);
}

void stopMotors() {
  digitalWrite(motorForwardPin, LOW);
  digitalWrite(motorBackwardPin, LOW);
  digitalWrite(motorLeftPin, LOW);
  digitalWrite(motorRightPin, LOW);
}
