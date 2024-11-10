import struct
import sys

# Get first parameter from command line as the hex value
hex_value = sys.argv[1]

print("Argument Value :", hex_value)

# Example data from one notification
hex_data = bytes.fromhex(hex_value)

# Decoding as little-endian 4-byte integers
value1, value2, value3 = struct.unpack('<3I', hex_data[:12])
last_byte = hex_data[12]
single_byte_status = hex_data[13]

print("Value 1:", value1)
print("Value 2:", value2)
print("Value 3:", value3)
print("Last Byte (status):", last_byte)
print("Single Byte Status:", single_byte_status)