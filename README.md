# mutekey

## Setup

1. Plug your neokey in and double-click the reset button. You should now see a mass storage device called `TRINKEYBOOT`.
2. Go to [circuitpython.org](https://circuitpython.org/board/adafruit_neokey_trinkey_m0/) and download the latest CircuitPython 7.x release.
3. Copy the downloaded `.uf2` file to the `TRINKEYBOOT` device. It should now reboot and appear as `CIRCUITPY`.
4. Copy over all 3 `.py` files.
5. Edit the `config.py` to your heart's content.
6. Set up your operating system to use the key combination to mute/unmute your mic. I use `pactl` commands on linux, and [micmute](https://github.com/Anc813/MicMute) on windows.


## Configuration

### `hideMassStorage`

If enabled, your neokey won't show up as a mass storage device anymore.
You can get access to it again by pressing the big button while resetting/plugging in,
and holding it down until the colorwheel starts.
Resetting again will hide mass storage again.

### `keepLedOn`

When you press the touch button, the colorwheel will stop.
If true, it will stay on the current color, otherwise the LED will turn off.

In "mute"-mode, the touch button does nothing.

### `muteKeyCombination` and `unmuteKeyCombination`

Key combination to send when pressing the button.
Possible keycodes can be found in the [circuitpython documentation](https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html).


## Troubleshooting

### If you can't get mass storage to enable again

1. Connect to the neokey:

```shell
screen /dev/ttyACM0 115200
```

2. Remove `boot.py` from device:

* Press ctrl+c
* Press enter
* Run:
```python
import storage
import os
storage.remount('/', readonly=False)
os.remove('boot.py')
```

3. And press the reset button
