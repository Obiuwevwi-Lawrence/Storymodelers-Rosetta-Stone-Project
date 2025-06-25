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
| **Environmental Sensors** | CO2, Temp, Humidity, Light | Measures ambient environmental conditions |
| **Audio Interface** | ReSpeaker Mic Array         | Captures speech and sound for analysis        |
| **Processing Unit** | Raspberry Pi 5              | Runs AI models, records data, handles storage |
| **Power Supply** | 2x LiPo 3.7V 10,000mAh Batteries | Portable operation                           |
| **Enclosure**   | 3D-printed Custom Casing        | Protects components, enhances portability     |
| **Future Expansion** | Physiological Sensors (e.g., Heart Rate, GSR) | Emotional arousal detection pipeline    |

---

## 📊 High-Level Architecture Diagram

_See `docs/images/system_diagram.png` for a visual overview._  


