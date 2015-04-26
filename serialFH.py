CR = '\n'
LF = '\r'
ESC = 'c'
TIMEOUT = 0.5

import sys
import msvcrt
import serial
import time

# COM3 open serial to FH
comFH = serial.Serial(4, timeout=1)  # COM5
# COM4 open serial to AX
comAX = serial.Serial(3, timeout=1)  # COM4

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
    if(strAX.find('test') == 0):
        comFH.write('MEASURE\n\r')  # start measure
        strFH = comFH.read(30)  # read FH
        comAX.write('SHIFT' + str(strFH) + '\n\r')
        comAX.write('message to AX\n')
        print 'Success SHIFT Command!!'
        print str(strFH)
    else:
        strAX = strFH
        comFH.write(strAX)
        print 'command is not SHIFT'
