# Acoustic-Animal-Repellent-System-Using-Animal-Detection

## Introduction
Agriculture is the backbone of many economies, providing food and livelihoods for billions of people worldwide. However, wildlife encroachment on farmlands poses challenges, leading to significant crop damage and economic losses. The proposed Acoustic Animal Repellent System aims to mitigate these challenges by utilizing sound frequencies to deter animals from entering agricultural fields.

## Problem Statement
Wildlife intrusions result in substantial economic losses for farmers, impacting food security and livelihoods. In regions with significant forest cover like India, the risk of wild animal attacks on agricultural fields is particularly high.

## Objectives
The primary objective of this project is to design and implement an innovative Acoustic Animal Repellent System that utilizes sound frequencies to deter animals from entering agricultural fields. Key objectives include:
- Integrating IR night vision cameras with computer vision algorithms and ultrasonic alarm systems to detect and deter intruding animals.
- Developing a cost-effective, environmentally friendly, and easy-to-deploy system for agricultural use.

## Implementation
### 1. Installing IR Night Vision Cameras
IR cameras are strategically placed in farm areas with high animal activity to capture images both day and night for the pusrpose of data generation. As of now we are placing the IR camera in our college campus farm area where wild boar , peacock , cow come for grazing. For the generation of dataset we are integrating Raspberrypi 4B with IMX219 IR cut camera to capture the image only when motion is detected.

### 2. Computer Vision Algorithm for detecting Animals 
We are using Yolov8n model , which we will train on our custom data for the detection of animal.

### 3. Ultrasonic Alarm System
Ultrasonic alarm systems will be positioned in the farm to emit frequencies tailored to deter specific types of animals detected by the Animal Detection algorithm.

## Conclusion
The Acoustic Animal Repellent System offers a promising solution to mitigate crop damage caused by wildlife intrusions. By integrating advanced technologies like computer and sound frequency generation, the system aims to protect agricultural fields effectively while minimizing environmental impact. Further Detection and testing will be conducted to ensure the system's effectiveness and scalability for widespread agricultural use.
