from oled import *
from machine import Pin, I2C

i2c = I2C(scl=Pin(14), sda=Pin(12))
oled = SSD1306_I2C(128, 64, i2c)

def dataOutput(temp='00.00C', pres='0000.00hPa', tempDht='123', humDht='123'):
    oled.fill(0)
    oled.text('temp: ' + temp, 0, 0)
    oled.text('pres: ' + pres, 0, 10)
    oled.text('(/>_<)/ DHT ', 0, 20)
    oled.text('temp: ' + str(tempDht) + 'C', 0, 30)
    oled.text('hum: ' + str(humDht) + '%', 0, 40)

    oled.show()
