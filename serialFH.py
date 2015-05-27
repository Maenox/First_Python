CR = '\n'
LF = '\r'
ESC = 'c'

import sys
import msvcrt
import serial
import time
import string

# COM2 open serial to FH
comFH = serial.Serial(
    port=0,
    baudrate=38400,
    bytesize=8,
    stopbits=1,
    timeout=0.5)

# COM1 open serial to AX
comAX = serial.Serial(
    port=5,
    baudrate=19200,
    bytesize=7,
    stopbits=1,
    timeout=0.5)

while True:
    # C key is exit
    if msvcrt.kbhit():
        inp = msvcrt.getch()
        if(inp == ESC):
            comFH.flush()
            comAX.flush()
            comFH.close()
            comAX.close()
            break

    strAX = comAX.read(20)
    strFH = comFH.read(128)
    # if command from AX
    if(strAX.find('SHIFT 1') == 0):
        comFH.write('MEASURE\r')  # start measure
        strFH = comFH.read(128)  # read F
        if(strFH.find('OK') == 0):
            comAX.write('SHIFT ' + strFH[4:60] + '\n')
            print 'Success SHIFT 1 Command!!'
    elif(strAX.find('SHIFT 2') == 0):
        comFH.write('MEASURE\r')  # start measure Backprint
        strFH = comFH.read(128)
        if(strFH.find('OK') == 0):
            comAX.write('SHIFT ' + strFH[57:] + '\n')
            print 'Success SHIFT 2 Command!!'
    elif(strAX.find('SHIFT 3') == 0):
        comFH.write('MEASURE\r')  # start measure Backprint
        print 'Success SHIFT 3 Command!!'
    else:
        strAX = strFH
        comFH.write(strAX)
        print '.',
