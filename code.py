import time
import board
import digitalio
import neopixel
import rainbowio
import touchio
import usb_hid
import config
from adafruit_hid.keyboard import Keyboard

kbd = Keyboard(usb_hid.devices)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = config.brightness

button = digitalio.DigitalInOut(board.SWITCH)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

touch = touchio.TouchIn(board.TOUCH)

cachedColor = 0x00FF00
colorwheel = 0
muted = False
buttonStillPressed = True
touchStillPressed = False
showColorwheel = True

print("neokey up")

while True:
    if button.value and not buttonStillPressed:
        buttonStillPressed = True
        muted = not muted
        if muted:
            for key in config.muteKeyCombination:
                kbd.press(key)
            time.sleep(0.01)
            kbd.release_all()
            pixel[0] = config.muteColor
        else:
            for key in config.unmuteKeyCombination:
                kbd.press(key)
            time.sleep(0.01)
            kbd.release_all()

    if buttonStillPressed and not button.value:
        buttonStillPressed = False

    if touch.value and not muted and not touchStillPressed:
        touchStillPressed = True
        showColorwheel = not showColorwheel
        if not showColorwheel:
            cachedColor = pixel[0]

    if touchStillPressed and not touch.value:
        touchStillPressed = False

    if not muted:
        if showColorwheel:
            colorwheel = (colorwheel + config.colorwheelSpeed) % 255
            pixel[0] = rainbowio.colorwheel(colorwheel)
        elif config.keepLedOn:
            pixel[0] = cachedColor
        else:
            pixel[0] = 0x0

    time.sleep(0.01)
