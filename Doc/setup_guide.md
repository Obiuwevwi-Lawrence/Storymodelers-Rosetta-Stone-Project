# 🛠 Storymodelers' Rosetta Stone — Full Setup Guide

This document provides complete, step-by-step instructions to assemble, configure, and deploy the Rosetta Stone device for capturing team dynamics, environmental data, and speech using AI-enabled components.

---

## 📦 Hardware Assembly & Requirements

### Required Components

| Component                     | Model/Specification             |
|-------------------------------|----------------------------------|
| **Microcontroller**           | ESP32-WROOM-32 or equivalent    |
| **Processing Unit**            | Raspberry Pi 5 (8GB recommended) |
| **Microphone Array**           | ReSpeaker 2-Mic Array for Pi    |
| **CO2 Sensor**                 | SGP30 or equivalent             |
| **Temperature & Humidity Sensor** | BME280 Combined Sensor      |
| **Light Sensor**               | VEML7700                        |
| **Batteries**                  | 2x LiPo 3.7V 10,000mAh         |
| **Enclosure**                  | Custom 3D-printed (provided)    |
| **Wiring Materials**           | Jumper wires, headers, basic tools |

---

### Wiring Instructions

- **ESP32 I2C Connections**
   - SDA (Data) → GPIO21  
   - SCL (Clock) → GPIO22  
   - Power → 3.3V or 5V (as per sensor)  
   - Ground → GND  

- **ESP32 to Raspberry Pi Communication**
   - UART or I2C depending on your configuration

- **Sensor Connections**
   - CO2 Sensor → I2C  
   - Temp & Humidity Sensor → I2C  
   - Light Sensor → I2C  

- **Audio Interface**
   - ReSpeaker connects directly to Raspberry Pi GPIO or USB

⚠️ **Important:** Double-check wiring before connecting batteries or powering the system.

---

## 🔌 Hardware Assembly Steps

1. Print the enclosure from the provided STL file (`hardware/enclosure_design.stl`).
2. Mount all sensors securely inside the enclosure.
3. Wire all components as instructed above.
4. Insert ESP32 and Raspberry Pi 5 into the enclosure.
5. Connect and secure LiPo batteries, ensuring correct voltage and polarity.

---

## 💻 Required Software & Tools

| Tool                      | Purpose                           |
|---------------------------|-----------------------------------|
| **Arduino IDE**           | Flash ESP32 firmware              |
| **Python 3 (>=3.7)**      | Run Raspberry Pi scripts          |
| **pip3**                  | Install Python dependencies       |
| **Git**                   | Clone project repository          |
| **Google Cloud SDK** *(optional)* | Cloud storage management |

---

## ⚙️ ESP32 Firmware Upload

1. Download and install [Arduino IDE](https://www.arduino.cc/en/software).
2. Install ESP32 board package:
   - Open Arduino IDE  
   - Go to `File > Preferences`  
   - Add this URL to "Additional Board Manager URLs":  
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - Go to `Tools > Board > Board Manager`, search "ESP32", install latest package.
3. Connect ESP32 via USB.
4. Open `software/esp32/sensor_firmware.ino`.
5. Select:
   - Board: `ESP32 Dev Module`
   - Port: Your ESP32 serial port
6. Click `Upload`.

---

## 🐍 Raspberry Pi Software Installation

### Initial Setup

```bash
sudo apt update
sudo apt install python3-pip git
