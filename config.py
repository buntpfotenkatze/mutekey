from adafruit_hid.keycode import Keycode

# you can enable this for release builds
# WARNING: it's annoying to disable this again
hideMassStorage = False

# keep the LED on when disabling rainbow mode
keepLedOn = True

# brightness of the LED
brightness = 0.3

# speed of the rainbow changing
rainbowSpeed = 0.4

# color of the LED when muted. default: red
muteColor = 0xFF0000

# key combination to send on mute
muteKeyCombination = [
    Keycode.LEFT_SHIFT,
    Keycode.LEFT_CONTROL,
    Keycode.LEFT_ALT,
    Keycode.M,
]

# key combination to send on unmute
unmuteKeyCombination = [
    Keycode.LEFT_SHIFT,
    Keycode.LEFT_CONTROL,
    Keycode.LEFT_ALT,
    Keycode.PAUSE,
]
