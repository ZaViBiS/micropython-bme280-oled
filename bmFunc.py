from bm280 import *
from machine import Pin, I2C

i2c = I2C(scl=Pin(0), sda=Pin(4), freq=10000)
bm = BME280(i2c=i2c)

temp = lambda : bm.temperature # Температура

hum = lambda : bm.humidity # Влажность

pres = lambda : bm.pressure # Давление

allIndicators = lambda : [temp, hum, pres] # Список всех показателей
