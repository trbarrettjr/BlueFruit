import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.25
red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    x, y, z = cp.acceleration
    if y > 0:
        cp.pixels.fill(blue)
    elif y < 0:
        cp.pixels.fill(red)