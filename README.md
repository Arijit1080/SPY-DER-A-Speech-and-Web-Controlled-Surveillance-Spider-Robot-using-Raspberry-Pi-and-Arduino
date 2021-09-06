# SPY-DER : A speech & Web Controlled Surveillance Spider Robot using Raspberry Pi & Arduino
These are the codes and diagrams of one my recent project SPY-DER, a speech and web controlled robotics spider, built using Raspberry Pi and Arduino. It also has a inbuilt camera in it, so that it can do live surveillance (that's why we named it SPY-DER).

You can get the instructions to build this project from here: 

You can download the STL files from https://www.thingiverse.com/thing:4815137

## Components
I have used the following components in this project:
a) Arduino Nano (Required)
b) Raspberry Pi Zero W
c) Raspberry Pi camera
d) 5v to 3.3v Logic level shifter
e) Nano 328P Expansion Adapter Breakout Board IO Shield (Required)
f) SG90 Mini Servo 12 pieces (Required)
g) Buck Converter Lm2596
h) Lithium Ion Battery 2 pieces
i) Leds * 2 piece
j) Jumper Wires

## Requirements
Python 3.7.3
Flask 1.0.2

## Run
To run the web control interface:
```
cd web_control
python3 web_control.py
```
To run the speech control system:
```
cd picovoice
python3 demo/python/picovoice_demo_mic.py 
	--keyword_path resources/porcupine/resources/keyword_files/raspberry-pi/bumblebee_raspberry-pi.ppn  
	--context_path your_rhino_model
```

## Acknowledgments

* https://picovoice.ai/
* https://elinux.org/RPi-Cam-Web-Interface

