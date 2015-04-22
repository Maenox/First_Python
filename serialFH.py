#coding: utf-8
#AX2PCの通信
import sys
import serial
import time
#COM2を開く。ポートは0から数えるので通常COM1は0番目のポートである
com01 = serial.Serial(2, timeout=1)
#com02 = serial.Serial(3, timeout=1)

#COM1に書きこむ
com01.write('SHIFT 20,10,0,0,0,0\r')

while True:
    str = com01.read(30)
    print str
    time.sleep(10)


#終わったらclose
#続けて書きこむ場合はいちいちcloseしなくてもいい
com01.close()
com02.close()
