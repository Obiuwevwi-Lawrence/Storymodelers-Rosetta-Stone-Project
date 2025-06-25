# 🛠️ Storymodelers' Rosetta Stone — Sensor & Component Specifications

This document details the hardware components integrated into the Rosetta Stone device, including sensors, processing units, and power systems. It also outlines future planned expansions for physiological sensing.

---

## 📦 Core Components

| Component                | Model/Specification               | Function                                |
|--------------------------|-----------------------------------|------------------------------------------|
| **Microcontroller**      | ESP32-WROOM-32 or compatible      | Reads environmental sensors, communicates with Raspberry Pi |
| **Processing Unit**      | Raspberry Pi 5 (8GB recommended)  | Runs AI models, records and processes data |
| **Audio Interface**      | ReSpeaker 2-Mic Array for Pi      | Captures speech, sound, and voice data  |
| **Power System**         | 2x LiPo 3.7V 10,000mAh Batteries  | Provides portable, rechargeable power   |
| **Enclosure**            | 3D-Printed Custom Housing (STL provided) | Protects components, enhances portability |

---

## 🌡️ Environmental Sensors

| Sensor Type        | Model               | Measurement Range     | Function                          |
|--------------------|--------------------|-----------------------|-----------------------------------|
| **CO2 Sensor**     | Adafruit SGP30 or equivalent | 400 to 60,000 ppm  | Measures carbon dioxide levels    |
| **Temperature Sensor** | BME280 Combined Sensor | -40°C to +85°C       | Ambient temperature monitoring    |
| **Humidity Sensor** | BME280 Combined Sensor | 0% to 100% RH         | Relative humidity monitoring      |
| **Light Sensor**    | VEML7700            | 0 to 120,000 lux       | Measures environmental light levels |

---

## 🗂️ Planned Future Expansions

| Component                | Target Model (Planned)            | Function                           |
|--------------------------|-----------------------------------|-------------------------------------|
| **Physiological Sensor - Heart Rate** | Optical PPG or ECG Sensor (TBD) | Detects heart rate and variability |
| **Physiological Sensor - GSR/EDA** | Skin Conductance Sensor (TBD) | Measures electrodermal activity, indicates emotional arousal |
| **Microphone Upgrade**   | 4-Mic or 6-Mic Array (optional)  | Enhanced spatial audio capture     |
| **AI Model Upgrades**    | Local emotion detection, topic modeling | Deeper real-time interaction analysis |

---

## 🪛 Physical and Electrical Details

- **ESP32 I/O Pins Used:**
   - I2C SDA: GPIO21
   - I2C SCL: GPIO22
   - UART TX/RX: Custom based on wiring

- **Sensor Power Requirements:**
   - 3.3V or 5V depending on sensor
   - Ensure regulated supply for accuracy

- **Audio Interface:**
   - Connects via USB or GPIO to Raspberry Pi 5

- **Battery Operation:**
   - Dual LiPo 3.7V in parallel or series (confirm setup)
   - Provides hours of continuous recording

---

**Refer to [hardware/bill_of_materials.xlsx](../hardware/bill_of_materials.xlsx) for full component ordering details.**

---
