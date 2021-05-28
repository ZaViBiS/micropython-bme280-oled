from bmFunc import *
from oledFunc import *
from machine import Pin, I2C
from time import sleep
import network
import dht

button = Pin(5, Pin.IN, Pin.PULL_UP)
d = dht.DHT11(Pin(13))

def offWifi():
    network.WLAN(network.STA_IF).active(False)
    network.WLAN(network.AP_IF).active(False)

def pokazDolgihDanih():
    tempirature = 0
    press = 0
    dht_tempirature = 0
    dht_press = 0

    for x in range(100):
        tempirature += float(temp().replace('C', ''))
        press += float(pres().replace('hPa', ''))

        dht_data = dhtData
        dht_tempirature += dht_data[0]
        dht_press += dht_data[1]

        sleep(0.1)

    tempirature = round( tempirature / 100, 2)
    press = round(press / 100, 2)

    dht_tempirature = round(dht_tempirature / 100, 2)
    dht_press = round(dht_press / 100, 2)

    tempirature = str(tempirature)
    press = str(press)

    print('temperature : ' + tempirature)
    print('humidity : ' + hum())
    print('pressure : ' + press)
    dataOutput(tempirature, press, dht_data[0], dht_data[1])

def dhtData():
    d.measure()

    return [d.temperature(), d.humidity()]

def pokazDanih():
    dht_data = dhtData()

    print('temperature : ' + temp())
    print('humidity : ' + hum())
    print('pressure : ' + pres())
    dataOutput(temp(), pres(), dht_data[0], dht_data[1])


