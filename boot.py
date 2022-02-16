import storage
import board
import digitalio
import config

storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "MUTEKEY"
storage.remount("/", readonly=True)

if config.hideMassStorage:
    button = digitalio.DigitalInOut(board.SWITCH)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN

    if not button.value:
        print("disabling usb drive")
        storage.disable_usb_drive()
