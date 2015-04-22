#coding: utf-8
#FH2PCの通信
CR = ' '
LF = ' '
ESC = 'ESC'
TIMEOUT = 0.5

import sys
import msvcrt
import serial
import time

#COM2を開く。ポートは0から数えるので通常COM1は0番目のポートである
com01 = serial.Serial(2, timeout=1)
#com02 = serial.Serial(3, timeout=1)

#COM1に書きこむ
com01.write('SHIFT 20,10,0,0,0,0\r')

while True:
    if msvcrt.kbhit():
        inp = msvcrt.getch()
        if(inp == ESC):
            break
    str = com01.read(30)
    print str
    time.sleep(1)

#終わったらclose
#続けて書きこむ場合はいちいちcloseしなくてもいい
com01.close()
