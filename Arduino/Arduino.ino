/*
  https://playground.arduino.cc/Interfacing/Python
  Using FastLED library:
  - Download the FastLED library: http://fastled.io/ as .zip.
  - In Arduino IDE: Sketch -> Include library -> Add .ZIP library
*/
#include <FastLED.h>
#define NUM_LEDS 240
#define DATA_PIN 6

// INITIATORS FOR SERIAL COMMUNICATION
String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete

// INITIATORS FOR LEDS AND LED UPDATE MODE
CRGB leds[NUM_LEDS];

// Function for reading data from serial and setting corresponding LEDS
// Each led has 3 bytes of data (One for each color value)
void setLedsFromInputString(String input){
  uint8_t value;
  int ledCount = 0;
  int colorCount = 0;
  int lastSpaceIndex = 0;
  for(int i = 0; i <= input.length(); i++){
    if(input[i] == ' '){
      currentSpaceIndex = i;
      value = uint8_t(input.substring(lastSpaceIndex+1, currentSpaceIndex).toint());
      lastSpaceIndex = currentSpaceIndex;
      switch colorCount{
        case 0:
          leds[ledCount].r = value;
          break;
        case 1:
          leds[ledCount].g = value
          break;
        case 2:
          leds[ledCount].b = value;
          break;
      }
      colorCount++;
      if(colorCount == 3){
        colorCount = 0;
        ledCount++;
      }
    }
  }
}

// SETUP AND MAIN LOOP
void setup(){
  Serial.begin(9600);              //Starting serial communication
  inputString.reserve(NUM_LEDS*3); //Buffer for incoming data
  // randomSeed(analogRead(0));
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
}

void loop(){
  // Handle incoming serial data from PC, Pioneer LX or Raspberry Pi
  if(stringComplete){
    //Serial.println(inputString);
    setLedsFromInputString(inputString);
    inputString = "";
    stringComplete = false;
    FastLed.show();
  }
  delay(1);
}

// SERIAL
/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.

  https://www.arduino.cc/en/Reference/SerialEvent
  https://www.arduino.cc/en/Tutorial/SerialEvent
*/
void serialEvent(){
  while(Serial.available()){
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
