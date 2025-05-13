# Storymodelers-Rosetta-Stone-Project

## 🎯 Objective:
Develop a compact, intelligent, and portable device that captures speech and environmental signals during real-world meetings, delivering actionable insights via embedded AI.

## 🚀 Positioning:
This is not merely a sensor hub—it is a participatory AI teammate, capable of observing, interpreting, and enhancing human interaction. It aligns with the AFOSR, MURI, and Minerva themes on team science, situational awareness, and adaptive decision-making support.

## 🔹 2. Phase 1: Discovery & Requirements Analysis
🔍 Key Steps:

Stakeholder Interviews: Capture perspectives from engineers, social scientists, and intended end-users.

Literature Review: Identify best practices and gaps from works by Fiore, Cooke, Seeber, etc.

## Use Case Modeling:

📌 Scenario 1: Boardroom decision-making

📌 Scenario 2: Interdisciplinary research teams

📌 Scenario 3: High-stakes negotiation sessions


## 🔹 3. Phase 2: System Architecture & Prototyping
## 🔧 Hardware Stack:

Raspberry Pi 5: Central processing and AI inference

ESP32: Manages environmental sensing and wireless connectivity

ReSpeaker Mic Array: Directional, multi-speaker speech capture

Sensors: Light, CO₂, Temperature, Humidity (expandable to VOCs and others)

## 💻 Software Stack:

Linux OS + Python

On-device Speech Recognition: Whisper or Vosk

Signal Processing: SciPy, OpenCV (future video support)

Cloud Upload: Google Cloud Storage with secure REST API

## 🛠 Prototyping Approach:

Test-Driven Development (TDD)

Modular hardware and software design

Over-the-air (OTA) firmware update readiness

## 🔹 4. Phase 3: AI Integration & Analytics Layer
🧠 Key AI Features:

Speech Analytics: Transcription, speaker turns, tone/interruption patterns

Environmental Analytics: Real-time insight into meeting conditions

Arousal Mapping (Future): Sync with GSR/HR data for emotional peaks

## 🧩 Model Considerations:

Lightweight, real-time inference models

Embedding and summarization for storage efficiency and privacy

Optional Edge TPU upgrade for future performance scaling

## 🔹 5. Phase 4: Testing & Validation
🧪 Testing Areas:

Functional: Verify audio, sensors, uploads, and control interfaces

Performance: Real-time benchmarks and responsiveness

Reliability: Extended 8-hour session stress testing

Security: Cloud encryption and penetration tests

📊 Pilot Study:

Run in 3 controlled environments

Collect user feedback via survey forms

Compare human feedback with system-captured insights

