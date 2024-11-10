import struct
import sys

# Function to parse hex data from the notification string
def extract_hex_data(notification):
    # Split the notification string and filter out non-hex characters
    hex_data = notification.split('Value:')[1].strip().replace('  ', ' ').split()
    # Convert hex data into a byte array
    return bytes.fromhex(' '.join(hex_data))

# Main script to process the notification
def main():
    # Ensure the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py '<full_notification_string>'")
        sys.exit(1)

    # Get the full notification string from the command-line argument
    notification = sys.argv[1]

    # Extract hex data from the notification
    try:
        hex_data = extract_hex_data(notification)

        # Decode the first 12 bytes as three 4-byte integers in little-endian format
        value1, value2, value3 = struct.unpack('<3I', hex_data[:12])

        # Extract the last two bytes as single bytes
        last_byte = hex_data[12]
        single_byte_status = hex_data[13] if len(hex_data) > 13 else None

        # Print the decoded values
        print("Value 1 (Integer 1):", value1)
        print("Value 2 (Integer 2):", value2)
        print("Value 3 (Integer 3):", value3)
        print("Last Byte (power or some status):", last_byte)

        if single_byte_status is not None:
            print("Single Byte Status:", single_byte_status)
        else:
            print("Single Byte Status: Not available")

    except (IndexError, ValueError) as e:
        print("Error processing the notification data:", e)

if __name__ == "__main__":
    main()