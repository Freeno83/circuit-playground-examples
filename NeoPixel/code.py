# Circuit Playground NeoPixel
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# choose which demos to play
# 1 means play, 0 means don't!
color_chase_demo = 0
flash_demo = 0
rainbow_demo = 0
rainbow_cycle_demo = 1

delay = 0.1 # Increase the number to slow down

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

ALL_COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 10) + j * 5
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)


while True:
    if color_chase_demo:
        for c in ALL_COLORS:
            color_chase(c, delay)

    if flash_demo:
        for c in ALL_COLORS:
            pixels.fill(c)
            pixels.show()
            time.sleep(delay)

    if rainbow_cycle_demo:
        rainbow_cycle(delay)

    if rainbow_demo:
        rainbow(delay)
