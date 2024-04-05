# Hospital IoT Project with Fall Detection and Automated Lighting Control

In this project, we have developed a smart system using MicroPython, focusing on patient safety and energy efficiency within a hospital environment. Our system integrates motion detection, fall detection, and automated lighting control to enhance patient care and optimize energy usage.

## Project Overview
In a hospital setting, patient safety is of paramount importance. Accidental falls can lead to serious injuries, and energy consumption must be managed efficiently. Our IoT project addresses these concerns by implementing the following key features:

* Fall Detection: Utilizing motion detection sensors strategically placed near beds, our system can detect falls accurately. Upon detecting a fall, the system triggers alerts, notifying hospital staff promptly to provide assistance to the patient.

* Automated Lighting Control: The lighting system within the hospital is automated based on the time of day. Lights are automatically turned off during the daytime to conserve energy and turned on in the evening for better visibility. Additionally, during the night, main lights are turned off, and night lights are activated to ensure a comfortable environment for patients while minimizing disturbance.

## System Architecture
Our system consists of the following main components:

* Microcontroller: We use a microcontroller to interface with various sensors, control lights, and manage communication with IoT platforms.

* Motion Detection Sensors (PIR): Passive Infrared (PIR) sensors are deployed near patient beds to detect motion accurately.

* Alert System: In the event of a fall detection, the system triggers alert lights and sends notifications to hospital staff members for immediate assistance.

* Automated Lighting System: The lighting system is controlled automatically based on predefined time schedules, ensuring energy efficiency and patient comfort.

## Code Overview
Python code used in our project, written in MicroPython, which runs on the microcontroller. The code includes functions for:

1. Establishing Wi-Fi connection for IoT communication.
2. Sending status updates to the ThingSpeak IoT platform.
3. Configuring pins for PIR sensors, lights, and alert systems.
4. Implementing fall detection logic and automated lighting control based on time schedules.

## Implementation
1> Set up your microcontroller environment with MicroPython.
2> Connect the necessary hardware components, including PIR sensors, lights, and alert systems.
3> Write the code
4> Customize the code as needed to match your hardware configuration and requirements.
5> Upload the modified code to microcontroller and ensure proper functioning.
