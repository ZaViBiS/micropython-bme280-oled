from machine import Pin, I2C
import network

button = Pin(5, Pin.IN, Pin.PULL_UP)

def offWifi():
    network.WLAN(network.STA_IF).active(False)
    network.WLAN(network.AP_IF).active(False)
