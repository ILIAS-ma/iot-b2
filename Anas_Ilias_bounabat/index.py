#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <NewPing.h>

#define TRIGGER_PIN  12 
#define ECHO_PIN     11  
#define MAX_DISTANCE 200 

#define LED_PIN 13 

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

unsigned long previousMillis = 0; 
const long interval = 50;           

void setup() {
  Serial.begin(9600); 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); 
  display.clearDisplay();
  display.display(); 

  pinMode(LED_PIN, OUTPUT); 
}
void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;  
    display.clearDisplay();

    unsigned int distance = sonar.ping_cm();
    if (distance > 0) {

      robojaxText("Distance", 3, 0, 2, false);
      // Affichage de la distance mesurée au centre de l'écran
      robojaxText(String(distance) + " cm", 3, 20, 3, false);

      if (distance <= 10) {
        digitalWrite(LED_PIN, HIGH); 
      } else {
        digitalWrite(LED_PIN, LOW);  
      }
    } else {
      robojaxText("Distance out of range", 3, 20, 1, false);
    }
    display.display();
  }
  unsigned int distance = sonar.ping_cm();
  Serial.print("Ping: ");
  Serial.print(distance);
  Serial.println(" cm");
}

void robojaxText(String text, int x, int y, int size, boolean d) {
  display.setTextSize(size); 
  display.setTextColor(WHITE);
  display.setCursor(x, y); 
  display.println(text); 
  if (d) {
    display.display(); 
  }
}
