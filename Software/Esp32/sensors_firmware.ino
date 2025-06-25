#include <Wire.h>
#include <Adafruit_SGP30.h>
#include <Adafruit_BME280.h>
#include <Adafruit_VEML7700.h>
#include <WiFi.h>
#include <HTTPClient.h>

// Replace with your network credentials
const char* ssid = "*******";
const char* password = "*********";

const char* serverIP = "192.168.0.59";  // Raspberry Pi IP address
const int serverPort = 5000;            // Port on Raspberry Pi

// Create sensor objects
Adafruit_SGP30 sgp;
Adafruit_BME280 bme;
Adafruit_VEML7700 veml = Adafruit_VEML7700();

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22); // SDA, SCL

  // Initialize WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize BME280
  if (!bme.begin(0x76)) {
    Serial.println("Could not find BME280 sensor at address 0x76!");
    while (1);
  } else {
    Serial.println("BME280 sensor initialized at address 0x76");
  }

  // Initialize VEML7700
  if (!veml.begin()) {
    Serial.println("Could not find VEML7700 sensor!");
    while (1);
  } else {
    Serial.println("VEML7700 sensor initialized");
  }

  // Initialize SGP30
  if (!sgp.begin()) {
    Serial.println("Could not find SGP30 sensor!");
    while (1);
  } else {
    Serial.println("SGP30 sensor initialized");
  }

  // Wait for the SGP30 to be ready
  delay(1000);
}

void loop() {
  // Read BME280 data
  float temperature = bme.readTemperature();
  float humidity = bme.readHumidity();
  float pressure = bme.readPressure() / 100.0F;

  // Read VEML7700 data
  float lux = veml.readLux();

  // Read SGP30 data
  if (!sgp.IAQmeasure()) {
    Serial.println("SGP30 measurement failed");
    delay(2000);
    return;
  }
  uint16_t tvoc = sgp.TVOC;
  uint16_t eco2 = sgp.eCO2;

  // Print sensor data
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" *C, Humidity: ");
  Serial.print(humidity);
  Serial.print(" %, Pressure: ");
  Serial.print(pressure);
  Serial.print(" hPa, Light: ");
  Serial.print(lux);
  Serial.print(" lx, TVOC: ");
  Serial.print(tvoc);
  Serial.print(" ppb, eCO2: ");
  Serial.print(eco2);
  Serial.println(" ppm");

  // Send data to Raspberry Pi server
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String serverPath = "http://" + String(serverIP) + ":" + String(serverPort) + "/upload";

    http.begin(serverPath);
    http.addHeader("Content-Type", "application/json");

    // Create JSON data
    String jsonData = "{";
    jsonData += "\"temperature\":" + String(temperature) + ",";
    jsonData += "\"humidity\":" + String(humidity) + ",";
    jsonData += "\"pressure\":" + String(pressure) + ",";
    jsonData += "\"light\":" + String(lux) + ",";
    jsonData += "\"tvoc\":" + String(tvoc) + ",";
    jsonData += "\"eco2\":" + String(eco2);
    jsonData += "}";

    int httpResponseCode = http.POST(jsonData);  // Changed this line

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }

  delay(30000);  // Send data every 30 seconds
}
