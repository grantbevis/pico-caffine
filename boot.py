import storage
import usb_cdc
# Disable both serial devices.
usb_cdc.disable()
# Disable CIRCUITPY Mass Storage
storage.disable_usb_drive()