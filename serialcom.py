# import select
import sys
# import time
# import machine
import struct
import binascii

def sendData(mag, acc, ang):
    #print("test")
    packet = bytearray()
    packet.extend(bytearray.fromhex("0200a6bd"))
    for i in range(3):
        packet.extend(bytearray(struct.pack("f", mag[i])))
    for i in range(3):
        packet.extend(bytearray(struct.pack("f", acc[i])))
    for i in range(3):
        packet.extend(bytearray(struct.pack("f", ang[i])))
    # print(packet.hex())
    sys.stdout.buffer.write(packet)

# while True:
#     # Check if there is any data available on sys.stdin without blocking
#     if poll_obj.poll(0):
#         # Read one character from sys.stdin
#         ch = sys.stdin.read(1)
#         # Check if the character read is 't'
#         if ch=='r':
#             # Toggle the state of the LED
#             led.value(not led.value())
#             # Print a message indicating that the LED has been toggled
#             print ("LED toggled" )
#     # Small delay to avoid high CPU usage in the loop
#     time.sleep(0.1)