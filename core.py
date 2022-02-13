import time
import board
import digitalio
from neopixel import NeoPixel
import usb_hid
import storage
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# name usb drive
#storage.remount("/", readonly=False)
#m = storage.getmount("/")
#m.label = "MUTEKEY"
#storage.remount("/", readonly=True)
#storage.enable_usb_drive()
# storage.disable_usb_device()

pixel = NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.05
pixel[0] = 0x00FF00

button = digitalio.DigitalInOut(board.SWITCH)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

kbd = Keyboard(usb_hid.devices)

muted = False
buttonStillPressed = False

print("neokey up")

while True:
    if button.value and not buttonStillPressed:
        buttonStillPressed = True
        if muted:
            kbd.send(
                Keycode.LEFT_SHIFT, Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.PAUSE
            )
            pixel[0] = 0x00FF00
            muted = False
        else:
            kbd.send(
                Keycode.LEFT_SHIFT, Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.M
            )
            pixel[0] = 0xFF0000
            muted = True

    if buttonStillPressed:
        if not button.value:
            buttonStillPressed = False

    time.sleep(0.01)
