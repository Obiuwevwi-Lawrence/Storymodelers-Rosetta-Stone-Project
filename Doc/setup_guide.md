# 🛠 Storymodelers' Rosetta Stone — Setup Guide

This guide provides step-by-step instructions to assemble the hardware, configure software, and deploy the Rosetta Stone device for real-time speech capture, environmental monitoring, and AI-powered analysis.

---

## 📦 Hardware Assembly

**Required Components**
- 1x ESP32 Microcontroller
- 1x Raspberry Pi 5 (8GB recommended)
- 1x ReSpeaker 2-Mic Array for Raspberry Pi
- 1x CO2 Sensor (SGP30 or equivalent)
- 1x Temperature/Humidity Sensor (BME280)
- 1x Light Sensor (VEML7700)
- 2x LiPo 3.7V 10,000mAh Batteries
- 1x Custom 3D-printed Enclosure
- Connecting wires, headers, basic tools

**Assembly Steps**
1. Mount sensors onto the enclosure slots.
2. Wire sensors to ESP32:
   - I2C SDA → GPIO21
   - I2C SCL → GPIO22
   - Power (3.3V or 5V depending on sensor)
   - Ground connections
3. Connect ESP32 to Raspberry Pi 5 via UART or I2C.
4. Install ReSpeaker Mic Array onto Raspberry Pi.
5. Place Raspberry Pi and ESP32 inside enclosure.
6. Secure batteries; verify voltage and polarity.

⚠️ *Double-check wiring before powering the device.*

---

## 💻 Software Installation

**On Raspberry Pi 5**
```bash
sudo apt update
sudo apt install python3-pip git


