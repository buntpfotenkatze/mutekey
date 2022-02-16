# mutekey

## Config

### `hideMassStorage`

If you enabled `hideMassStorage`,
you can get access to it again by pressing the big button while resetting,
and holding it until the color wheel starts.
Resetting again will hide mass storage again.

## If you can't access the mass storage

Connect to neokey:

```shell
screen /dev/ttyACM0 115200
```

Remove `boot.py` from device:

* press ctrl+c
* press enter

```python
import storage
import os
storage.remount('/', readonly=False)
os.remove('boot.py')
```

And press the reset button
