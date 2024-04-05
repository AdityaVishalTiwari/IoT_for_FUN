# Hospital IoT Project with Fall Detection and Automated Lighting Control

This project utilizes MicroPython to create an IoT solution for hospital monitoring. It integrates motion detection systems with microcontrollers placed near patient beds, enabling real-time monitoring and automated response mechanisms. The system primarily focuses on fall detection and automated lighting control to enhance patient care and optimize energy usage.

## Project Overview
In a hospital setting, patient safety is of paramount importance. Accidental falls can lead to serious injuries, and energy consumption must be managed efficiently. This IoT project addresses these concerns by implementing the following key features:

* Fall Detection: Utilizing motion detection sensors strategically placed near beds, our system can detect falls accurately. Upon detecting a fall, the system triggers alerts, notifying hospital staff promptly to assist the patient.

* Automated Lighting Control: The lighting system within the hospital is automated based on the time of day. Lights are automatically turned off during the daytime to conserve energy and turned on in the evening for better visibility. Additionally, during the night, main lights are turned off, and night lights are activated to ensure a comfortable environment for patients while minimizing disturbance.

## System Architecture
Our system consists of the following main components:

* Microcontroller: We use a microcontroller to interface with various sensors, control lights, and manage communication with IoT platforms.

* Motion Detection Sensors (PIR): Passive Infrared (PIR) sensors are deployed near patient beds to detect motion accurately.

* Alert System: In the event of a fall detection, the system triggers alert lights and sends notifications to hospital staff members for immediate assistance.

* Automated Lighting System: The lighting system is controlled automatically based on predefined time schedules, ensuring energy efficiency and patient comfort.

## Requirements
* MicroPython-enabled microcontroller (e.g., ESP32)
* Passive Infrared (PIR) motion sensors
* LEDs or light sources
* Internet connectivity for IoT communication

## Code Overview
Python code used in our project, written in MicroPython, which runs on the microcontroller. The code includes functions for:

1. Establishing Wi-Fi connection for IoT communication.
2. Sending status updates to the ThingSpeak IoT platform.
3. Configuring pins for PIR sensors, lights, and alert systems.
4. Implementing fall detection logic and automated lighting control based on time schedules.

## Implementation
1) Set up your microcontroller environment with MicroPython.
2) Connect the necessary hardware components, including PIR sensors, lights, and alert systems.
3) Write the code.
4) Customize the code as needed to match your hardware configuration and requirements.
5) Upload the modified code to the microcontroller and ensure proper functioning.
