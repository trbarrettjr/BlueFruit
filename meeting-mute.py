"""
Project inspired by https://learn.adafruit.com/TeamsMuteButton

Their code uses the Arduino IDE.  I utilized their CircuitPython Library.

Project code is here: https://github.com/microsoft/teamsmutebutton
"""

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_circuitplayground import cp

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

while True:
    while cp.button_a and cp.switch: # For Zoom; Audio Toggle; Switch Left
        kbd.press(Keycode.GUI, Keycode.SHIFT, Keycode.A)
    while cp.button_b and cp.switch: # For Zoom; Video Toggle; Switch Left
        kbd.press(Keycode.GUI, Keycode.SHIFT, Keycode.V)
    while cp.button_a and not cp.switch: # For Google Meet; Audio Toggle; Switch Right
        kbd.press(Keycode.GUI, Keycode.D)
    while cp.button_b and not cp.switch: # For Google Meet; Video Toggle; Switch Right
        kbd.press(Keycode.GUI, Keycode.E)
    else:
        kbd.release_all()
