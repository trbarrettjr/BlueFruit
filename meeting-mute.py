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

button_a_pressed = False
button_b_pressed = False

while True:
    if cp.switch:
        if cp.button_a and not button_a_pressed:
            kbd.send(Keycode.GUI, Keycode.SHIFT, Keycode.A)
            button_a_pressed = cp.button_a
        elif not cp.button_a and button_a_pressed:
            button_a_pressed = cp.button_a
        if cp.button_b and not button_b_pressed:
            kbd.send(Keycode.GUI, Keycode.SHIFT, Keycode.V)
            button_b_pressed = cp.button_b
        elif not cp.button_b and button_b_pressed:
            button_b_pressed = cp.button_b
    else:
        if cp.button_a and not button_a_pressed:
            kbd.send(Keycode.GUI, Keycode.D)
            button_a_pressed = cp.button_a
        elif not cp.button_a and not button_a_pressed:
            button_a_pressed = cp.button_a
        if cp.button_b and not button_b_pressed:
            kbd.send(Keycode.GUI, Keycode.E)
            button_b_pressed = cp.button_b
        elif not cp.button_b and button_b_pressed:
            button_b_pressed = cp.button_b
