import pygatt
import binascii
import time

# Define the MAC address and UUID of the target device and characteristic
device_address = 'YOU_MAC_ADR_HERE'
characteristic_uuid = 'YOU_CHAR_UID_HERE'

# Define the hexadecimal command to send
command_str = "toggle"
hex_command = binascii.hexlify(command_str.encode()).decode()
byte_command = bytes.fromhex(hex_command)

# Create a Pygatt BLE adapter
adapter = pygatt.GATTToolBackend()

try:
    # Start the Pygatt adapter
    adapter.start()
    print('start')
    time.sleep(10)

    # Connect to the device
    device = adapter.connect(device_address)
    print('connect')
    time.sleep(10)

    # Send the command to the characteristic
    device.char_write(characteristic_uuid, byte_command)
    #time.sleep(1)
    device.char_write(characteristic_uuid, byte_command)
    #time.sleep(1)
    device.char_write(characteristic_uuid, byte_command)

finally:
    # Stop the Pygatt adapter
    adapter.stop()
