#coding: utf-8
#AX2PCの通信
CR = ' '
LF = ' '
ESC = 'c'
TIMEOUT = 0.5

import mscvrt
import serial
import time

#COM4を開く、AXとの通信
com02 = serial.Serial(3, timeout=1)

#COM1に書きこむ
com02.write('SHIFT 20,10,0,0,0,0\r')

while True:
    if msvcrt.kbhit():
        inp = msvcrt.getch()
        if(inp == ESC):
            break
    str = com02.read(30)
    print str
    time.sleep(1)

#終わったらclose
#続けて書きこむ場合はいちいちcloseしなくてもいい
com02.close()
