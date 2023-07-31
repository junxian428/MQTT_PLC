import requests
import time
import serial
import datetime


while True:
    with open('error.txt', 'r') as file:
        first_line = file.readline().strip()
        if(first_line== "1"):
            print("Error...........")
            print("Call WhatsAPP API")
            #r = requests.get("http://localhost:8000/EMERGENCY")
            #print(r.status_code)
            #print(r.headers)
            #print(r.content)  # bytes
        else:
            current_time = datetime.datetime.now()
            #r = requests.get("http://localhost:8000")
            #print(r.status_code)
            #print(r.headers)
            #print(r.content)  # bytes
            print("Success : Time now: " + str(current_time))

    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600,   bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

    # send data over serial communication
    message = b'@00RR0100000140*\r'
    #@00WR0100000145*
    #00wr0100FFFF44*
    #@00RR0004000145*\r
    #@00WR000400FF000F37*\r


    ser.write(message)
    with open('sending.txt', 'w') as file:
        file.write(message.decode())


    # read data from serial communication
    # data = ser.readline()
    # print(str(data))
     #while True:
    #    data = ser.read(1)
    #      if data:
    #         print(data)

    # close serial communication
    ser.close()

    time.sleep(5) 