import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(1)
led.value = False
time.sleep(1)
led.value = True
time.sleep(5)
 
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 
 
while True:
    led.value = False
    keyboard.send(Keycode.SHIFT)
    time.sleep(0.5)
    led.value = True
    time.sleep(66.6)
