# Raspberry Pi Pico Keyboard Emulator

Small python script to emulate a USB keyboard and caffinate the machine it's connected to. This will also hide the USB mass storage and serial devices from the host.

Written for [CircuitPython](https://circuitpython.org)

## Instructions

- Install [CircuitPython](https://circuitpython.org) on your Pico
- Copy this repository to the CIRCUITPY USB Mass Storage device
- Plug the Pico into another computer, the LED will stay illuminated for 66.6 seconds and blink when it sends a Shift key to the host.