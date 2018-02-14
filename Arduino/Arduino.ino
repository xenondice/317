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
uint8_t buffer[NUM_LEDS*3];
//String inputString = "";         // a String to hold incoming data
int numBytesRead = 0;   // How many bytes have we read into the buffer
bool gotData = false;

// INITIATORS FOR LEDS
CRGB leds[NUM_LEDS];

// Each led has 3 bytes of data (One for each color value)
void setLedsFromBuffer(){
  int colorCount = 0;
  int ledCount = 0;
  for(int i = 0; i< NUM_LEDS*3; i++){
    switch(colorCount){
        case 0:
          leds[ledCount].r = buffer[i];
          break;
        case 1:
          leds[ledCount].g = buffer[i];
          break;
        case 2:
          leds[ledCount].b = buffer[i];
          break;
      }
      colorCount++;
      if(colorCount == 3){
        colorCount = 0;
        ledCount++;
      }
  }

  /*
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
  */
}

// SETUP AND MAIN LOOP
void setup(){
  Serial.begin(57600);              //Starting serial communication
  //inputString.reserve(NUM_LEDS*3); //Buffer for incoming data
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  leds[0].r = 255;
  leds[1].g = 255;
  leds[2].b = 255;
  FastLED.show();
}

void loop(){
  // Handle incoming serial data from PC, Pioneer LX or Raspberry Pi
  if(gotData){
    //Serial.println(inputString);
    setLedsFromBuffer();
    gotData = false;
    FastLED.show();
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
  while(Serial.available() && !gotData){
    buffer[numBytesRead] = Serial.read();
    //inputString += inChar;
    numBytesRead++;
    if(numBytesRead == NUM_LEDS*3){
      gotData = true;
    }
  }
}
