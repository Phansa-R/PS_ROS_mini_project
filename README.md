# ROS Mini Project
## Description
This is ROS Miniproject for PP robot.
Control with Python GUI using Potentiometer and Encoder with Arduino UNO R3.

## Overview
- [ROS Mini Project](#ros-mini-project)
  - [Description](#description)
  - [Overview](#overview)
  - [Enlightening Influence](#enlightening-influence)
  - [CAD design](#cad-design)
    - [PART 1 Base](#part-1-base)
    - [PART 2 Joint1 prismatic](#part-2-joint1-prismatic)
    - [PART 3 Joint2 prismatic](#part-3-joint2-prismatic)
  - [Component](#component)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Setup](#setup)
    - [Installing](#installing)
    - [Creating package](#creating-package)
  - [Executing program](#executing-program)
    - [Hardware Connecting](#hardware-connecting)
    - [Software Ros workspace](#software-ros-workspace)
    - [Software Arduino](#software-arduino)
    - [Software Launch command](#software-launch-command)
  - [Authors](#authors)
    - [Member Team](#member-team)
    - [Support Team](#support-team)
  - [Acknowledgments](#acknowledgments)
 
## Enlightening Influence
I drew inspiration to design this robot from my experience with 3D printers. Consequently, I devised a system featuring one motor to regulate the X-axis and another for the Y-axis. Moreover, I incorporated a central mechanism resembling the functionality of a 3D printer, allowing for dynamic movement within the CAD design.

## CAD design
### PART 1 Base

<img src="https://github.com/Phansa-R/PS_ROS_mini_project/blob/main/cad_picture/base.jpg" width=35% height=35%>

### PART 2 Joint1 prismatic
(Prismatic using Potentiometer)

<img src="https://github.com/Phansa-R/PS_ROS_mini_project/blob/main/cad_picture/joint1.jpg" width=35% height=35%>

### PART 3 Joint2 prismatic
(Prismatic using Encoder)

<img src="https://github.com/Phansa-R/PS_ROS_mini_project/blob/main/cad_picture/joint2.jpg" width=35% height=35%>

### ASSEMBLY

<img src="https://github.com/Phansa-R/PS_ROS_mini_project/blob/main/cad_picture/assembly.jpg" width=35% height=35%>

## Component
### Hardware
* Arduino Mega 2560
* 50K Potentiometer
* KY-040 Rotary Encoder (WH-040)
* DRV8825 Stepper motor driver board (2 motors)
* Power supply
### Software
* Ubuntu 20.04
* ROS Noetic 
* Python3
* Arduino IDE 1.8.15

## Setup
### Installing
* Visual Studio Code
  - install CustomTkinter-Snippets V2.0.0
* Arduino IDE

### Creating package
We need to setup our new workspace with command-line tools `catkin_create_pkg`. Then we will create a new ROS package. 

Create a new Workspace: 
```
$ mkdir -p ~/dev/catkin_ws/src
$ cd ~/dev/catkin_ws/src
```
Create a new package and specify dependencies to include:
```
$ catkin_create_pkg pkg_name rospy
```
Build package
```
$ cd ~/catkin_ws
$ catkin_make
```

## Executing program
### Hardware Connecting
* Connect Potentiometer into Arduino using A0 pin on Arduino
  - (+) to 5V
  - GND to GND
* Connect Stepper motor
  - Power supply into Driver Board
    - Power supply 12V to VMOD
    - GND to GND
  - Stepper into Driver Board
    - A(Black) to 2A
* schematic diagram

  
### Software Ros workspace
Start a master node in a new terminal:
```
$ roscore
```
Open new terminal and go to source folder in your workspace:
```
$ cd catkin_ws/src
```
Clone all file in github repository by git clone command:
```
$ git clone https://github.com/Phansa-R/PS_ROS_mini_project.git
```
Go back to your workspace and `catkin_make` to complile your package:
```
$ cd ..
$ catkin_make
```
### Software Arduino
1. Open Firmware directory and continue to miniproject_arduino.
2. Copy code and upload it into your Arduino.
### Software Launch command
Start a master node in a new terminal.
```
$ roscore
```
Open new terminal and run this command on your terminal to launch code. Check your serial port on Arduino and replace in `port:="<--YOUR-PORT-->"`.
For example my serial port is USB0 then it will be `roslaunch robot_description robot_launch.launch port:="/dev/ttyUSB0"`.
```
$ roslaunch robot_description robot_launch.launch port:="<--YOUR-PORT-->"
``` 

## Authors
### Member Team 
* Nipitpon Phunchoedchan 6452500015
* Bhornpreeya Apibunprasert 6452500040
* Phansa Romruen 6452500155

### Support Team
* Chollatis Petchsing 6452500023
* Kantawit Panyateang 6452500198
* Thanita kaeoking 6452500244
* Komgrid Petchpayub 6452500392

## Acknowledgments
* [Potentiometer](https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial/)
* [Encoder WH-404](https://www.allnewstep.com/article/318/80-arduino-สอนวิธีการใช้งาน-สวิตช์รับข้อมูลแบบ-rotary-encoder)
* [Stepper Motor Control](https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/)


