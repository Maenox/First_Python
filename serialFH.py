#coding: utf-8
#FH2PCの通信
CR = ' '
LF = ' '
ESC = 'c'
TIMEOUT = 0.5

import sys
import msvcrt
import serial
import time

#COM3を開く、FHとの通信
com01 = serial.Serial(2, timeout=1)
#COM4を開く、AXとの通信
com02 = serial.Serial(3, timeout=1)

#中継
while True:
    #cキーで終了
    if msvcrt.kbhit():
        inp = msvcrt.getch()
        if(inp == ESC):
            break
            com01.close()
            com02.close()
    #strAX is str go to AX from FH
    strAX = com01.read(30)
    #AXからSHIFT命令が来たら
    if(strAX.find('SHIFT') == 0):
        com01.write('MEASURE\r')  #start measure
        strFX = com01.read(30)  #read FX
        com01.write('SHIFT' + str(strFX))
    else:
        com01.write(str(strFX))
