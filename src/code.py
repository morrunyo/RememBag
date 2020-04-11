"""Imports"""
from adafruit_circuitplayground.express import cpx
import time
import gc

"""Definitions"""
RED = (90, 0, 0)
GREEN = (0, 90, 0)
BLUE = (0, 0, 90)
WHITE = (30, 30, 30)
BLACK = (0, 0, 0)
YELLOW = (45, 45, 0)

"""Classes"""
class Mode:
    FIXED = 0
    BLINK = 1

class State:
    OFF = 0
    ON = 1
    
class Item:
    colour = WHITE
    state = State.OFF
    neopixel = 0
    
    def __init__(self, colour, state, neopixel):
        self.colour = colour
        self.state = state
        self.neopixel = neopixel

"""Functions"""
def processItems(blinkTimer):
    if mode == Mode.FIXED:
        blinkTimer = 0
    elif mode == Mode.BLINK:
        blinkTimer = blinkTimer + 1
        if blinkTimer == blinkFrequence:
            blinkTimer = 0
    for i in items:
        if mode == Mode.FIXED:
            if i.state == State.OFF:
                cpx.pixels[i.neopixel] = BLACK 
            elif i.state == State.ON:
                cpx.pixels[i.neopixel] = i.colour
        elif mode == Mode.BLINK:
            if i.state == State.OFF:
                cpx.pixels[i.neopixel] = BLACK 
            elif i.state == State.ON:
                if blinkTimer < blinkFrequence / 2:
                    cpx.pixels[i.neopixel] = i.colour
                elif blinkTimer >= blinkFrequence / 2:
                    cpx.pixels[i.neopixel] = BLACK
    next
    return blinkTimer

def selectItem(item):
    if mode == Mode.BLINK:
        if item.state == State.OFF:
            item.state = State.ON
        elif item.state == State.ON:
            item.state = State.OFF
    return 0

def processNotifications(blinkTimer):
    if mode == Mode.BLINK:
        if blinkTimer < blinkFrequence / 2:
            cpx.pixels[pixelMode.neopixel] = pixelMode.colour
        elif blinkTimer >= blinkFrequence / 2:
            cpx.pixels[pixelMode.neopixel] = BLACK
    elif mode == Mode.FIXED:
        cpx.pixels[pixelMode.neopixel] = BLACK
    return 0
 
def inactiveCircuit():
    for i in items:
        cpx.pixels[i.neopixel] = BLACK
    return 0
    
"""Main"""
print('Started!! {} free bytes'.format(gc.mem_free()))
mode = Mode.FIXED
blinkTimer = 0
activationTimer = 0
cpx.pixels.brightness = 0.3
blinkFrequence = 80
pixelMode = Item(WHITE, State.OFF, 5)
items = []
o0 = Item(RED, State.OFF, 0)
items.append(o0)
o1 = Item(GREEN, State.OFF, 1)
items.append(o1)
o2 = Item(BLUE, State.OFF, 2)
items.append(o2)
o3 = Item(YELLOW, State.OFF, 3)
items.append(o3)

while True:
    blinkTimer = processItems(blinkTimer)
    processNotifications(blinkTimer)
    
    if cpx.touch_A5:
        while cpx.touch_A5:
            pass
        if mode == Mode.FIXED:
            mode = Mode.BLINK
            print("Blink Mode")
        elif mode == Mode.BLINK:
            mode = Mode.FIXED
            print("Fixed Mode")
            time.sleep(0.1)
            activationTimer = 0
    if cpx.touch_A1:
        while cpx.touch_A1:
            pass
        selectItem(items[0])
        time.sleep(0.1)
        activationTimer = 0
    if cpx.touch_A2:
        while cpx.touch_A2:
            pass        
        selectItem(items[1])
        time.sleep(0.1)
        activationTimer = 0
    if cpx.touch_A3:
        while cpx.touch_A3:
            pass
        selectItem(items[2])
        time.sleep(0.1)
        activationTimer = 0
    if cpx.touch_A4:
        while cpx.touch_A4:
            pass
        selectItem(items[3])
        time.sleep(0.1)
        activationTimer = 0
        
    if mode == Mode.FIXED:
        activationTimer = activationTimer + 1
    if activationTimer > blinkFrequence * 10:
        inactiveCircuit()
        while not (cpx.shake() or cpx.touch_A1 or cpx.touch_A2 or cpx.touch_A3 or cpx.touch_A4 or cpx.touch_A5):
            pass
        activationTimer=0
