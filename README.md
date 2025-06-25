# 🪨 Storymodelers' Rosetta Stone

**An AI-Enabled Device for Capturing, Analyzing, and Modeling Human Team Dynamics**

---

## 📖 Overview

The Storymodelers' Rosetta Stone is a portable, sensor-integrated AI system designed to capture multimodal data during real-world team interactions. By combining speech, environmental, and physiological signals, the device enables advanced analysis of group dynamics, emotional arousal, and communication patterns in collaborative environments.

Originally developed for research into AI-human teaming, participatory research, and interdisciplinary collaboration, the Rosetta Stone provides an open foundation for studying human interaction in meetings, workshops, clinical settings, or field studies.

---

## 🚀 Key Features

✅ Speech Detection and Transcription  
✅ Environmental Sensing (CO2, Temperature, Humidity, Light)  
✅ Team Dynamics and Interaction Analysis  
✅ Emotional Arousal Detection Pipeline (In Progress)  
✅ Real-Time Audio Recording and Cloud Upload  
✅ AI-Powered Meeting Summarization and Moderation Support  
✅ Fully Portable, Rechargeable Design  
✅ Modular Sensor Integration for Future Expansion  

---

## 🛠 System Components

| Component             | Description                                           |
|----------------------|-------------------------------------------------------|
| **ESP32**            | Microcontroller handling environmental sensors        |
| **ReSpeaker Mic Array** | Captures speech and sound in the environment       |
| **Raspberry Pi 5**   | Central AI unit for processing, transcription, and storage |
| **CO2 Sensor**       | Monitors carbon dioxide levels                        |
| **Temperature/Humidity Sensor** | Tracks ambient conditions                 |
| **Light Sensor**     | Measures environmental light intensity                |
| **LiPo Batteries**   | Dual 3.7V 10,000mAh for portable operation            |
| **Enclosure**        | Custom 3D-printed housing for device protection       |

*Planned*: Integration of physiological sensors (e.g., heart rate, GSR) and emotional analysis.

---

## 🌍 Use Case Examples

- Multidisciplinary Team Research  
- Participatory AI Workshops  
- Meeting Moderation and Feedback  
- Team Science and Collaboration Studies  
- Clinical Communication Analysis  
- Military or High-Stakes Team Interaction Research  

---

## ⚡ Quick Start

**Hardware Setup**
1. Assemble sensors and microcontrollers as per [docs/architecture.md](docs/architecture.md)
2. Ensure batteries are charged and securely connected

**Software Installation**
```bash
# On Raspberry Pi 5
git clone https://github.com/YourUsername/storymodelers-rosetta-stone.git
cd storymodelers-rosetta-stone/software/raspberry_pi
pip install -r requirements.txt
python recorder.py
