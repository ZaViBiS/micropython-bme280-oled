from functions import *
from bmFunc import *
from oledFunc import *
import time

offWifi() # Выключить wifi

while True:
    if button.value():
        print('temperature : ' + temp())
        print('humidity : ' + hum())
        print('pressure : ' + pres())
        dataOutput(temp(), pres())

    time.sleep(0.1)
