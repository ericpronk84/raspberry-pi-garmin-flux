import struct
import sys

def extract_hex_data_clean(notification):
    # Split the notification string to isolate the hex values
    # Remove any trailing parts that contain non-hex data (e.g., ASCII representations)
    hex_data_part = notification.split()[0:16]  # Takes the first 16 hex segments (or adjust as needed)

    print("clean data 1:", hex_data_part)

    # Filter out invalid characters and join the hex parts to create a clean string
    clean_hex_data = ' '.join([segment for segment in hex_data_part if all(c in '0123456789abcdefABCDEF' for c in segment)])

    print("clean data: ", clean_hex_data)
    return bytes.fromhex(clean_hex_data)

def main():
    if len(sys.argv) != 2:
        print("Usage: python decode_notification.py '<notification_line>'")
        sys.exit(1)

    notification = sys.argv[1]

    try:
        hex_data = extract_hex_data_clean(notification)
        value1, value2, value3 = struct.unpack('<3I', hex_data[:12])
        last_byte = hex_data[12]
        single_byte_status = hex_data[13] if len(hex_data) > 13 else None

        print("Value 1 (Integer 1):", value1)
        print("Value 2 (Integer 2):", value2)
        print("Value 3 (Integer 3):", value3)
        print("Last Byte (status):", last_byte)

        if single_byte_status is not None:
            print("Single Byte Status:", single_byte_status)
        else:
            print("Single Byte Status: Not available")

    except (IndexError, ValueError) as e:
        print("Error processing the notification data:", e)

if __name__ == "__main__":
    main()