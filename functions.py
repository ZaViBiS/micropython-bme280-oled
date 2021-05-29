from bmFunc import *
from oledFunc import *
from machine import Pin, I2C
import time
import network
import dht
import json

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

        time.sleep(0.1)

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
    writeData(tempirature, press)

def pokazDanih():
    dht_data = dhtData()
    bData = [temp(), hum(), pres()]

    print('temperature : ' + bData[0])
    print('humidity : ' + bData[1])
    print('pressure : ' + bData[2])
    dataOutput(bData[0], bData[2], float(dht_data[0]), float(dht_data[1]))
    # writeData(bData[0], bData[2])

def jsonReader(): # Чтение файла
    with open('data.json') as file:
        data = json.load(file)
    return data

def writeData(temp, pres):
    data = jsonReader()
    data['temp'].append([temp])
    data['pres'].append([pres])

    jsonWriter(data)

'''
def writeData(temp, pres):
    with fileinput.FileInput('data.json', inplace=True, backup='.bak') as file:
        for line in file:
            line = line.rstrip()  # remove trailing (invisible) space
            print('новое' if line == 'старое' else line)  # stdout is redirected to the file
    os.unlink(filename + '.bak') # remove the backup on success
'''

def jsonWriter(data): # Запись в файл
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
