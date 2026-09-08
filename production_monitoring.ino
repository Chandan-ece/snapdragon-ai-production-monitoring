/*
  Snapdragon AI Lab - Production Monitoring Prototype
  ESP32 + 2 IR/Optical Sensors

  Sensor 1: GPIO 27
  Sensor 2: GPIO 26
  Serial output: timestamp,count,sensor1,sensor2

  Change GPIO numbers if your physical wiring is different.
*/

const int SENSOR_1 = 27;
const int SENSOR_2 = 26;

unsigned long totalCount = 0;
unsigned long lastSensor1 = 0;
unsigned long lastSensor2 = 0;
const unsigned long debounceMs = 300;

void setup() {
  Serial.begin(115200);
  pinMode(SENSOR_1, INPUT_PULLUP);
  pinMode(SENSOR_2, INPUT_PULLUP);
}

void loop() {
  unsigned long now = millis();

  int s1 = digitalRead(SENSOR_1);
  int s2 = digitalRead(SENSOR_2);

  if (s1 == LOW && now - lastSensor1 > debounceMs) {
    totalCount++;
    lastSensor1 = now;
  }

  if (s2 == LOW && now - lastSensor2 > debounceMs) {
    totalCount++;
    lastSensor2 = now;
  }

  Serial.printf("%lu,%lu,%d,%d\n", now, totalCount, s1, s2);
  delay(1000);
}
