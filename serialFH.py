CR = '\n'
LF = '\r'
ESC = 'c'
TIMEOUT = 0.5

import sys
import msvcrt
import serial
import time

# COM3 open serial to FH
comFH = serial.Serial(
    port=1,
    baudrate=19200,
    bytesize=7,
    stopbits=1
    timeout=0)

# COM4 open serial to AX
comAX = serial.Serial(
    port=0,
    baudrate=19200,
    bytesize=7,
    stopbits=1,
    timeout=5)  # COM4

while True:
    # C key is exit
    if msvcrt.kbhit():
        inp = msvcrt.getch()
        if(inp == ESC):
            comFH.close()
            comAX.close()
            break

    strAX = comAX.read(30)
    strFH = comFH.read(30)
    # if command from AX
    if(strAX.find('SHIFT 1') == 0):
        comFH.write('MEASURE /C\r')  # start measure
        strFH = comFH.read(3)  # read FH
        if(strFH.find('OK') == 0):
            strFH.read(30)
            comAX.write('SHIFT' + str(strFH) + '\r')
            print 'Success SHIFT Command!!'
            comAX.write('MEASURE /E\r')  # Stop Measure
        else:

            print 'Bad MEASURE...'
        print str(strFH)
    else:
        strAX = strFH
        comFH.write(strAX)
        #print 'command is not SHIFT'
        print strAX
