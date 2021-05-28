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

def dhtData():
    d.measure()

    return [d.temperature(), d.humidity()]

def pokazDolgihDanih():
    tempirature = 0
    press = 0
    dht_tempirature = 0
    dht_press = 0
    raz = 10 # Количество считований 

    for x in range(raz):
        tempirature += float(temp().replace('C', ''))
        press += float(pres().replace('hPa', ''))

        d.measure()
        dht_tempirature += d.temperature()
        dht_press += d.humidity()

        sleep(0.1)

    tempirature = round( tempirature / raz, 2)
    press = round(press / raz, 2)

    dht_tempirature = round(dht_tempirature / raz, 2)
    dht_press = round(dht_press / raz, 2)

    tempirature = str(tempirature) + 'C'
    press = str(press) + 'hPa'

    print('temperature : ' + tempirature)
    print('humidity : ' + hum())
    print('pressure : ' + press)
    dataOutput(tempirature, press, dht_tempirature, dht_press)

def pokazDanih():
    dht_data = dhtData()

    print('temperature : ' + temp())
    print('humidity : ' + hum())
    print('pressure : ' + pres())
    dataOutput(temp(), pres(), float(dht_data[0]), float(dht_data[1]))


