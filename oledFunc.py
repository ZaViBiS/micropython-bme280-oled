from oled import *
from machine import Pin, I2C

i2c = I2C(scl=Pin(14), sda=Pin(12))
oled = SSD1306_I2C(128, 64, i2c)

def dataOutput(temp='00.00C', pres='0000.00hPa'):
    oled.fill(0)
    oled.text('temp : ' + temp, 0, 0)
    oled.text('pres : ' + pres, 0, 10)
    oled.show()