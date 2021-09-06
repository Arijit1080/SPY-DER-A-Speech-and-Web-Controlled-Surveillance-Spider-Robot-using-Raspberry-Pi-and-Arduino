# SPY-DER : A speech & Web Controlled Surveillance Spider Robot using Raspberry Pi & Arduino
These are the codes and diagrams for one of my recent project SPY-DER, a speech and web controlled robotics spider, built using Raspberry Pi and Arduino. It also has a inbuilt camera in it, so that it can do live surveillance (that's why we named it SPY-DER).

You can get the instructions to build this project from here: 

You can download the STL files from https://www.thingiverse.com/thing:4815137

## Components
I have used the following components in this project:
1. Arduino Nano (Required)
2. Raspberry Pi Zero W
3. Raspberry Pi camera
4. 5v to 3.3v Logic level shifter
5. Nano 328P Expansion Adapter Breakout Board IO Shield (Required)
6. SG90 Mini Servo 12 pieces (Required)
7. Buck Converter Lm2596
8. Lithium Ion Battery 2 pieces
9. Leds * 2 piece
10. Jumper Wires

## Requirements
1. Python 3.7.3
2. Flask 1.0.2

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

