# coding: utf-8
CR = '\n'
LF = '\r'
ESC = 'c'
TIMEOUT = 0.5

import sys
import msvcrt
import serial
import time

# COM3を開く、FHとの通信
comFH = serial.Serial(4, timeout=1)  # COM5
# COM4を開く、AXとの通信
comAX = serial.Serial(3, timeout=1)  # COM4

#中継
while True:
    #cキーで終了
    if msvcrt.kbhit():
        inp = msvcrt.getch()
        if(inp == ESC):
            comFH.close()
            comAX.close()
            break

    strAX = comAX.read(30)
    strFH = comFH.read(30)
    # AXからSHIFT命令が来たら
    if(strAX.find('test') == 0):
        comFH.write('MEASURE\r\n')  # start measure
        strFH = comFH.read(30)  # read FH
        comAX.write('SHIFT' + str(strFH) + '\n')
        comAX.write('message to AX\n')
        print 'Success SHIFT Command!!'
        print str(strFH)
    else:
        strAX = strFH
        comFH.write(strAX)
        print 'command is not SHIFT'
