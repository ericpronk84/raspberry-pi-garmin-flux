from bleak import BleakClient
from RPLCD.i2c import CharLCD

# Replace this with your trainer's MAC address and the UUID of the Power Measurement characteristic
DEVICE_MAC = "D4:D4:83:33:33:18"
POWER_MEASUREMENT_UUID = "00002a63-0000-1000-8000-00805f9b34fb"  # Standard UUID for cycling power measurement

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()
lcd.write_string('Connecting to Tacx Flux 59711')

def notification_handler(sender, data):
    """
    Handle incoming notifications from the power measurement characteristic.
    """
    # Convert the raw byte data into a readable format
    hex_data = [f"{byte:02x}" for byte in data]
    print(f"Raw Data: {hex_data}")

    # Decode the power field (assuming it's the 2nd and 3rd bytes, little-endian)
    power_bytes = data[2:4]
    power = int.from_bytes(power_bytes, byteorder="little")
    print(f"Power (Watts): {power}")

    # Convert the integer to a string
    power_str = str(power)

    lcd.clear()
    lcd.write_string(f"Power: {power_str} W")


async def main():
    async with BleakClient(DEVICE_MAC) as client:

        lcd.clear()
        lcd.write_string('Connected')

        # Subscribe to notifications for the power measurement characteristic
        await client.start_notify(POWER_MEASUREMENT_UUID, notification_handler)
        print("Listening for power data. Press Ctrl+C to stop.")

        try:
            while True:
                await asyncio.sleep(1)  # Keep the script running
        except KeyboardInterrupt:
            print("Stopping notifications...")
            await client.stop_notify(POWER_MEASUREMENT_UUID)
            lcd.clear()
            lcd.write_string('Disconnected')

# Run the main function
import asyncio
asyncio.run(main())