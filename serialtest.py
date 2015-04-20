#coding: utf-8
from serial import Serial

#COM2を開く。ポートは0から数えるので通常COM1は0番目のポートである
com01 = Serial(2)

#COM1に書きこむ
com01.write('SHIFT 20,10,0,0,0,0\n\r')

#終わったらclose
#続けて書きこむ場合はいちいちcloseしなくてもいい
com01.close()
