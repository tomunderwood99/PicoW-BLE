Sending strings to a Pico W using BLE
=============
This is an example of how to send strings from a computer to a Pico W over BLE. In the future I hope to send JSON objects in an optimized way to control the Pico W

## Basis
This is based off of the [Electrocredible guide](https://electrocredible.com/raspberry-pi-pico-w-bluetooth-ble-micropython/). For this, you will need to flash a Pico W with [this specific UF2](https://datasheets.raspberrypi.com/soft/micropython-firmware-pico-w-130623.uf2). This is originally found labelled as the 'Raspberry Pi Pico W with Wi-Fi and Bluetooth LE support' UF2 in this [documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html). In the future you may be able to use the generic MicroPython release, but the current version (v1.20.0) does not support bluetooth.

After installing the correct UF2 outlined above, copy the three python files from the pico_files folder onto your pico. These are pulled directly from the Electrocredible guide linked above. When 'test_ble.py' is run, it starts BLE advertising for the Pico. I prefer not to name this 'main.py' as this naming convention will automatically run the script on boot. 

Next, download the 'pygatt_demo.py' file onto your RPI (or other computer) and install the required packages, likely just pygatt. Update the MAC address and Characteristic UUID. With the Pico W still advertising, you can run this script and it should connect and send the toggle command 3 times, which you can monitor on Thonny, or watch the Pico LED blink!

I'll update this soon with more details on finding your MAC address and Characteristic UUID, but you can probably find those if you ask ChatGPT for help. Also, it appears that the bluetooth connection may mess with my Raspberry Pi's wifi connection, likely related to interference and weak antennas

Good luck, and feel free to reach out if you need help.

Thomas
