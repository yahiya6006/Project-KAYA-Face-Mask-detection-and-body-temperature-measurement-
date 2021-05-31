/*In this arduino code we are going to program MLX90614 IR thermal sensor.
Remember:
------------------------------------------------------------------------
1. MLX is working on 3.3v logic
------------------------------------------------------------------------
*/

const int PIN_vltageIN =A0; // This pin is used to read the input voltage of the sensor 
const float Operating_voltage = 3.3;//Operating voltage of Arduino. either 3.3V or 5.0V 
#include <Wire.h>
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();
float Ambient_data, Object_data;
float data,x;
void setup() {
  Serial.begin(19200);
  mlx.begin();
}

void loop() {
  delay(100);
  Object_data = mlx.readObjectTempC();
  Ambient_data = mlx.readAmbientTempC();
  
  int voltageIN = analogRead(PIN_vltageIN);
  float voltage =  voltageIN * (Operating_voltage / 1023.0);
  
  data = Object_data - (voltage -3) * 0.6;
  Ambient_data = Ambient_data - (voltage -3) * 0.6; 

  if ((Ambient_data - data) < (-1))
  {
    Serial.println(data);
  }
  //Serial.println(data);
  /*Serial.println("==========================");
  Serial.print("Objec Temperature :");
  Serial.println(data);
  Serial.print("Ambient Temperature :");
  Serial.println(Ambient_data);
  Serial.println("==========================");
  Serial.println("");*/
}
