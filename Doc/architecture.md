# 🏗️ Storymodelers' Rosetta Stone System Architecture

---

## 📖 Overview

The Rosetta Stone is a modular, AI-enabled device designed to capture, process, and analyze human team interactions. It combines environmental sensing, speech detection, and AI models to enable real-time meeting analysis, emotional arousal detection, and participatory AI applications.

This document outlines the complete hardware and software architecture, data flow, and system components of the Rosetta Stone.

---

## 🔧 System Components

| Category       | Component                         | Function                                      |
|----------------|-----------------------------------|-----------------------------------------------|
| **Microcontroller** | ESP32                       | Reads environmental sensor data               |
| **Environmental Sensors** | CO2, Temp, Pressure, Humidity, Light | Measures ambient environmental conditions |
| **Audio Interface** | ReSpeaker Mic Array         | Captures speech and sound for analysis        |
| **Processing Unit** | Raspberry Pi 5              | Runs AI models, records data, handles storage |
| **Power Supply** | 2x LiPo 3.7V 10,000mAh Batteries | Portable operation                           |
| **Enclosure**   | 3D-printed Custom Casing        | Protects components, enhances portability     |
| **Future Expansion** | Physiological Sensors (e.g., Heart Rate, GSR) | Emotional arousal detection pipeline    |

---

## 📊 High-Level Architecture Diagram

_See `docs/images/system_diagram.png` for a visual overview._  


---

## 🔄 Data Flow Summary

1. **Environmental Data Collection**  
   ESP32 reads environmental sensors via I2C and transmits data to the Raspberry Pi 5 via UART or I2C.

2. **Speech Detection & Recording**  
   ReSpeaker captures audio, passed to Raspberry Pi for recording, diarization, and transcription.

3. **AI Processing**  
   Raspberry Pi 5 runs:
   - Speech-to-text transcription
   - Speaker segmentation (diarization)
   - Meeting interaction modeling (future)
   - Emotional arousal detection pipeline (planned)

4. **Data Storage**  
   - Processed data is stored locally and/or uploaded to Google Cloud Storage for analysis.

---

## 🧩 Modular Design Philosophy

The Rosetta Stone is designed with modularity in mind, allowing:
- Easy hardware upgrades (sensor additions, replacements)
- AI model swaps or retraining for new use cases
- Integration of physiological sensors in future phases

---

## 🔋 Power Considerations

The device is powered by dual LiPo 3.7V 10,000mAh batteries, supporting hours of continuous operation, ideal for workshops, meetings, and mobile deployments.

---

## 📅 Development Roadmap

✅ Environmental and Speech Data Capture  
✅ Basic Transcription and Diarization  
🟡 AI-Powered Meeting Moderation (In Progress)  
🟡 Emotional Arousal Detection (In Progress)  
🟡 Real-Time Feedback and Alerts (Planned)  

---

**For technical setup, see [docs/setup_guide.md](setup_guide.md)**  
**For component specifications, see [docs/sensor_specs.md](sensor_specs.md)**  

---

